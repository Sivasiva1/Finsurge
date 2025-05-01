import os
import threading
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime
import time
import re

# DB Credentials
DB_USER = 'traininguser'
DB_PASSWORD = 'Tra!n$pa$$'
DB_HOST = '192.168.19.18'
DB_PORT = '3306'
DB_NAME = 'TRAINING'

# SQLAlchemy engine
engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Table and column mappings
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

# File to Table mapping
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
def get_completed_files():
    with engine.begin() as conn:
        result = conn.execute(text("SELECT filename FROM monitor WHERE status = 'completed'"))
        return set(row[0] for row in result.fetchall())
    
# Check if a filename is still in progress or not done
def is_file_pending(filename):
    with engine.begin() as conn:
        result = conn.execute(
            text("SELECT status FROM monitor WHERE filename = :filename"),
            {"filename": filename}
        ).fetchone()
        if not result or result[0] != "completed":
            return True
    return False

def insert_to_db_safe(file_path, table_name, original_filename):
    try:
        insert_to_db(file_path, table_name, original_filename) 
    except Exception as e:
        print(f" Thread crash while processing {file_path}: {e}")

def insert_to_db(file_path, table_name, original_filename):
    start_time = datetime.now()

    with engine.begin() as conn:
        conn.execute(
            text("REPLACE INTO monitor (filename, start_time, status) VALUES (:filename, :start_time, :status)"),
            {"filename": original_filename, "start_time": start_time, "status": "in_progress"}
        )

    try:
       # Read CSV in chunks and insert into temp table
        first_chunk = True
        for chunk in pd.read_csv(file_path, chunksize=1000):
            mode = 'replace' if first_chunk else 'append'
            chunk.to_sql(f"temp_{table_name}", con=engine, if_exists=mode, index=False)
            first_chunk = False

        key_col, name_col = table_columns_map[table_name]

        with engine.begin() as conn:
            # Update existing
            conn.execute(text(f"""
                UPDATE {table_name} t
                JOIN temp_{table_name} tmp 
                ON t.{key_col} = tmp.{key_col} AND t.{name_col} = tmp.{name_col}
                SET t.Roles = tmp.Roles
            """))

            # Delete already existing from temp
            conn.execute(text(f"""
                DELETE tmp FROM temp_{table_name} tmp
                JOIN {table_name} t 
                ON t.{key_col} = tmp.{key_col} AND t.{name_col} = tmp.{name_col}
            """))

            # Insert new ones
            conn.execute(text(f"""
                INSERT INTO {table_name} ({key_col}, {name_col}, Roles)
                SELECT {key_col}, {name_col}, Roles FROM temp_{table_name}
            """))

            conn.execute(text(f"TRUNCATE TABLE temp_{table_name}"))

        end_time = datetime.now()
        total_time = f"{(end_time - start_time).total_seconds():.2f} seconds"

        with engine.begin() as conn:
            conn.execute(
                text("""
                    UPDATE monitor 
                    SET end_time = :end_time, total_time_taken = :total_time, status = 'completed'
                    WHERE filename = :filename
                """),
                {"end_time": end_time, "total_time": total_time, "filename": original_filename}
            )

        print(f" Loaded '{original_filename}' into '{table_name}'")

    except Exception as e:
        end_time = datetime.now()
        total_time = f"{(end_time - start_time).total_seconds():.2f} seconds"

        with engine.begin() as conn:
            conn.execute(
                text("""
                    UPDATE monitor 
                    SET end_time = :end_time, total_time_taken = :total_time, status = :status
                    WHERE filename = :filename
                """),
                {"end_time": end_time, "total_time": total_time, "status": f"failed: {e}", "filename": original_filename}
            )
        print(f" Failed to load '{original_filename}': {e}")

def load_all_csvs(folder_path):
    threads = []
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    completed_files = get_completed_files() 

    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            original_filename = re.sub(r'(_\d{14})+\.csv$', '.csv', file)
            original_path = os.path.join(folder_path, file)

            if original_filename in table_map:
                if original_filename in completed_files:
                    print(f" Skipping '{original_filename}' (already completed)")
                    continue

                table_name = table_map[original_filename]

                # Rename file locally with timestamp
                base_name = original_filename.replace(".csv", "")
                timestamped_name = f"{base_name}_{timestamp}.csv" 
                new_path = os.path.join(folder_path, timestamped_name)
                os.rename(original_path, new_path)
                print(f" Renamed '{file}' → '{timestamped_name}'")

                t = threading.Thread(target=insert_to_db_safe, args=(new_path, table_name, original_filename)) 
                threads.append(t)
                t.start()
            else:
                print(f" Unknown file '{file}' — skipping")

    for t in threads:
        t.join()

    print("\n Folder scan complete.\n")

# Continuous background process
if __name__ == '__main__':
    folder = r"C:\Users\Nagaraja\Downloads\Training Finsurge-Siva M-Python\Training Finsurge\threadanddb\csv_files"
    while True:
        print(f"\n Checking folder at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...")
        load_all_csvs(folder)
        time.sleep(15)  
