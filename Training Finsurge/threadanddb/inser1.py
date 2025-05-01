import os
import threading
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime
import time
import re
import shutil
import logging
import logging

# === DB Config ===
DB_USER = 'traininguser'
DB_PASSWORD = 'Tra!n$pa$$'
DB_HOST = '192.168.19.18'
DB_PORT = '3306'
DB_NAME = 'TRAINING'
engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# === Table Maps ===
table_columns_map = {
    "interns": ("id", "internname"),
    "hr": ("id", "hrname"),
    "emps": ("id", "internname"),
    "teachers": ("id", "teachername"),
    "students": ("id", "studentname"),
    "principals": ("id", "principalname"),
    "workers": ("id", "workername"),
    "clerks": ("id", "clerkname"),
    "managers": ("id", "managername"),
    "staffs": ("id", "staffname"),
}
table_map = {
    "teachers.csv": "teachers",
    "students.csv": "students",
    "principals.csv": "principals",
    "workers.csv": "workers",
    "clerks.csv": "clerks",
    "employees.csv": "emps",
    "hrs.csv": "hr",
    "managers.csv": "managers",
    "staffs.csv": "staffs",
    "interns.csv": "interns"
}

# === Folder Setup ===
BASE_FOLDER = r"C:\Users\Nagaraja\Downloads\Training Finsurge-Siva M-Python\Training Finsurge\threadanddb"
IN_FOLDER = os.path.join(BASE_FOLDER, "IN")
OUT_FOLDER = os.path.join(BASE_FOLDER, "OUT")
NOT_PROCESSED_FOLDER = os.path.join(BASE_FOLDER, "NOT_PROCESSED")
DATAERROR_FOLDER = os.path.join(NOT_PROCESSED_FOLDER, "dataerror")

# === Logger Setup ===
LOG_FILE = os.path.join(BASE_FOLDER, "csv_loader.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger()

for folder in [IN_FOLDER, OUT_FOLDER, NOT_PROCESSED_FOLDER, DATAERROR_FOLDER]:
    os.makedirs(folder, exist_ok=True)

# === Utilities ===
def get_completed_files():
    with engine.begin() as conn:
        result = conn.execute(text("SELECT filename FROM monitor WHERE status = 'completed'"))
        return set(row[0] for row in result.fetchall())

def is_mysql_running():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return True
    except Exception as e:
        logging.warning(f"MySQL not reachable: {e}")
        return False

def move_file(src_path, dest_folder):
    try:
        dest = os.path.join(dest_folder, os.path.basename(src_path))
        shutil.move(src_path, dest)
        logging.info(f"Moved file to: {dest}")
    except Exception as e:
        logging.error(f"Failed to move file: {e}")

# === DB Insert Safe Wrapper ===
def insert_to_db_safe(file_path, table_name, original_filename):
    if is_mysql_running():
        try:
            insert_to_db(file_path, table_name, original_filename)
            move_file(file_path, OUT_FOLDER)
        except Exception as e:
            logging.error(f"Insertion failed for {file_path}: {e}")
            move_file(file_path, NOT_PROCESSED_FOLDER)
    else:
        logging.warning(f"MySQL down. Moving {file_path} to NOT_PROCESSED.")
        move_file(file_path, NOT_PROCESSED_FOLDER)

# === DB Insert Core ===
def insert_to_db(file_path, table_name, original_filename):
    start_time = datetime.now()
    logging.info(f"Start inserting: {file_path} into {table_name}")
    with engine.begin() as conn:
        conn.execute(text("INSERT INTO monitor (filename, start_time, status) VALUES (:filename, :start_time, :status)"),
                     {"filename": original_filename, "start_time": start_time, "status": "in_progress"})

    try:
        first_chunk = True
        for chunk in pd.read_csv(file_path, chunksize=1000):
            chunk.to_sql(f"temp_{table_name}", con=engine, if_exists='replace' if first_chunk else 'append', index=False)
            first_chunk = False

        key_col, name_col = table_columns_map[table_name]
        with engine.begin() as conn:
            conn.execute(text(f"""
                UPDATE {table_name} t
                JOIN temp_{table_name} tmp ON t.{key_col} = tmp.{key_col} AND t.{name_col} = tmp.{name_col}
                SET t.Roles = tmp.Roles;
            """))
            conn.execute(text(f"""
                DELETE tmp FROM temp_{table_name} tmp
                JOIN {table_name} t ON t.{key_col} = tmp.{key_col} AND t.{name_col} = tmp.{name_col};
            """))
            conn.execute(text(f"""
                INSERT INTO {table_name} ({key_col}, {name_col}, Roles)
                SELECT {key_col}, {name_col}, Roles FROM temp_{table_name};
            """))
            conn.execute(text(f"TRUNCATE TABLE temp_{table_name}"))

        end_time = datetime.now()
        total_time = f"{(end_time - start_time).total_seconds():.2f} seconds"

        with engine.begin() as conn:
            conn.execute(text("""
                UPDATE monitor 
                SET end_time = :end_time, total_time_taken = :total_time, status = 'completed'
                WHERE filename = :filename
            """), {"end_time": end_time, "total_time": total_time, "filename": original_filename})

        logging.info(f"Inserted {file_path} into {table_name} in {total_time}")

    except Exception as e:
        end_time = datetime.now() 
        total_time = f"{(end_time - start_time).total_seconds():.2f} seconds" 
        with engine.begin() as conn:
            conn.execute(text("""
                UPDATE monitor 
                SET end_time = :end_time, total_time_taken = :total_time, status = :status
                WHERE filename = :filename
            """), {"end_time": end_time, "total_time": total_time, "status": f"failed: {e}", "filename": original_filename})

        logging.error(f"Error processing {file_path}: {e}")
        raise e

# === Load CSVs ===
def load_all_csvs(folder_path):
    threads = []
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    completed_files = get_completed_files()

    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            original_filename = re.sub(r'(_\d{14})+\.csv$', '.csv', file)
            original_path = os.path.join(folder_path, file)

            if original_filename in table_map and original_filename not in completed_files:
                table_name = table_map[original_filename]
                base_name = original_filename.replace(".csv", "")
                timestamped_name = f"{base_name}_{timestamp}.csv"
                new_path = os.path.join(folder_path, timestamped_name)
                os.rename(original_path, new_path)

                logging.info(f"Starting thread for: {timestamped_name}")
                t = threading.Thread(target=insert_to_db_safe, name=f"Loader-{base_name}", args=(new_path, table_name, original_filename))
                threads.append(t)
                t.start()
            else:
                logging.info(f"Skipping {file} (already processed or unknown)")

    for t in threads:
        t.join()

# === Retry Failed ===
def monitor_not_processed_folder():
    while True:
        try:
            if is_mysql_running():
                for file in os.listdir(NOT_PROCESSED_FOLDER):
                    if file.endswith(".csv") and not file.startswith("retry_"):
                        original_filename = re.sub(r'(_\d{14})+\.csv$', '.csv', file)
                        if original_filename in table_map:
                            table_name = table_map[original_filename]
                            file_path = os.path.join(NOT_PROCESSED_FOLDER, file)
                            retry_path = os.path.join(NOT_PROCESSED_FOLDER, f"retry_{file}")
                            
                            try:
                                shutil.move(file_path, retry_path)  # prevent double processing
                                logging.info(f"[RETRY THREAD] Retrying file: {retry_path}")
                                insert_to_db(retry_path, table_name, original_filename)
                                move_file(retry_path, OUT_FOLDER)
                            except Exception as e:
                                error_str = str(e).lower()
                                if any(err in error_str for err in ["doesn't match", "expected", "wrong number of columns", "valueerror", "could not convert", "dataerror", "typeerror", "invalid", "column", "mismatch"]):
                                    move_file(retry_path, DATAERROR_FOLDER)
                                    logging.error(f"[RETRY THREAD] Moved {file} to DATAERROR folder due to data error.")
                                else:
                                    move_file(retry_path, NOT_PROCESSED_FOLDER)
                                    logging.warning(f"[RETRY THREAD] Retry failed for {file}, will try again later.")
            else:
                logging.warning("[RETRY THREAD] MySQL still not reachable, retry paused.")
        except Exception as e:
            logging.error(f"[RETRY THREAD] Unexpected error in retry loop: {e}")

        time.sleep(10)  # avoid tight loop

if __name__ == "__main__":
    # Start retry daemon
    daemon_thread = threading.Thread(target=monitor_not_processed_folder, name="DaemonThread", daemon=True)
    daemon_thread.start()

    # Main thread continuously scans for new files
    while True:
        time.sleep(10) 
        logging.info(f"[MAIN THREAD] Scanning folder at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        load_all_csvs(IN_FOLDER)
        time.sleep(15)
