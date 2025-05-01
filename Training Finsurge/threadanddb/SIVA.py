import os
import threading
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime

# DB Credentials
DB_USER = 'traininguser'
DB_PASSWORD = 'Tra!n$pa$$'
DB_HOST = '192.168.19.18'
DB_PORT = '3306'
DB_NAME = 'TRAINING'

# SQLAlchemy engine
engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# File to Table mapping
table_map = {
    "teachers.csv": "teachers",
    "students.csv": "students",
    "principals.csv": "principals",
    "workers.csv": "workers",
    "clerks.csv": "clerks", 
    "employees.csv": "emps",
    "hrs.csv": "hr",
    "managers.csv":"managers",
    "staffs.csv":"staffs",
    "interns.csv":"interns" 
}

# Insert CSV into DB with monitoring
def insert_to_db_safe(file_path, table_name):
    try:
        insert_to_db(file_path, table_name)
    except Exception as e:
        print(f"Thread crash while processing {file_path}: {e}")

# Core insert logic
def insert_to_db(file_path, table_name):
    filename = os.path.basename(file_path)
    start_time = datetime.now()

    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO monitor (filename, start_time, status) VALUES (:filename, :start_time, :status)"),
            {"filename": filename, "start_time": start_time, "status": "in_progress"}
        )

    try:
        for chunk in pd.read_csv(file_path, chunksize=1000): 
            chunk.to_sql(table_name, con=engine, if_exists='append', index=False)
        print(f"{filename} → Loaded into '{table_name}'") 

        end_time = datetime.now()
        total_time = f"{(end_time - start_time).total_seconds():.2f} seconds"

        with engine.begin() as conn:
            conn.execute(
                text("""
                    UPDATE monitor 
                    SET end_time=:end_time, status=:status, total_time_taken=:total_time 
                    WHERE filename=:filename
                """),
                {"end_time": end_time, "status": "completed", "total_time": total_time, "filename": filename}
            )

    except Exception as e:
        end_time = datetime.now()
        total_time = f"{(end_time - start_time).total_seconds():.2f} seconds"
        with engine.begin() as conn:
            conn.execute(
                text("""
                    UPDATE monitor 
                    SET end_time=:end_time, status=:status, total_time_taken=:total_time 
                    WHERE filename=:filename 
                """),
                {"end_time": end_time, "status": f"failed: {str(e)}", "total_time": total_time, "filename": filename}
            ) 
        print(f" Error loading {filename}: {e}")

# Load all files using threads
def load_all_csvs(folder_path):
    threads = []
    for file in os.listdir(folder_path):
        if file.endswith('.csv'):
            full_path = os.path.join(folder_path, file) 
            table_name = table_map.get(file)
            if table_name: 
                t = threading.Thread(target=insert_to_db_safe, args=(full_path, table_name))
                threads.append(t)
                t.start()
            else:
                print(f"Skipping '{file}' — No table mapping found.")

    for t in threads:
        t.join()

    print("\n All files processed \n")

if __name__ == '__main__':
    folder = r"C:\Users\Nagaraja\Downloads\Training Finsurge-Siva M-Python\Training Finsurge\threadanddb\csv_files"
    load_all_csvs(folder)



import os
import threading
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime
import time  

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

# Insert CSV into DB with monitoring and UPSERT logic
def insert_to_db_safe(file_path, table_name):
    try:
        insert_to_db(file_path, table_name)
    except Exception as e:
        print(f"Thread crash while processing {file_path}: {e}")

def insert_to_db(file_path, table_name):
    base_filename = os.path.basename(file_path)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename_with_timestamp = f"{base_filename}_{timestamp}"
    start_time = datetime.now()

    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO monitor (filename, start_time, status) VALUES (:filename, :start_time, :status)"),
            {"filename": filename_with_timestamp, "start_time": start_time, "status": "in_progress"}
        )

    try:
        for chunk in pd.read_csv(file_path, chunksize=1000): 
            chunk.to_sql(f"temp_{table_name}", con=engine, if_exists='replace', index=False)

        key_col, name_col = table_columns_map[table_name]

        with engine.begin() as conn:
            # Update existing rows
            update_stmt = f"""
                UPDATE {table_name} t
                JOIN temp_{table_name} tmp ON t.{key_col} = tmp.{key_col} AND t.{name_col} = tmp.{name_col}
                SET t.Roles = tmp.Roles
            """
            conn.execute(text(update_stmt))

            # Delete updated rows from temp
            delete_stmt = f"""
                DELETE tmp FROM temp_{table_name} tmp
                JOIN {table_name} t ON t.{key_col} = tmp.{key_col} AND t.{name_col} = tmp.{name_col}
            """
            conn.execute(text(delete_stmt))

            # Insert only new records
            insert_stmt = f"""
                INSERT INTO {table_name} ({key_col}, {name_col}, Roles)
                SELECT {key_col}, {name_col}, Roles FROM temp_{table_name}
            """
            conn.execute(text(insert_stmt))

            # Truncate temp table
            conn.execute(text(f"TRUNCATE TABLE temp_{table_name}"))

        end_time = datetime.now()
        total_time = f"{(end_time - start_time).total_seconds():.2f} seconds"

        with engine.begin() as conn:
            conn.execute(
                text("""
                    UPDATE monitor 
                    SET end_time=:end_time, status=:status, total_time_taken=:total_time 
                    WHERE filename=:filename
                """),
                {"end_time": end_time, "status": "completed", "total_time": total_time, "filename": filename_with_timestamp}
            )

        print(f"{base_filename}  Loaded into '{table_name}' successfully")

    except Exception as e:
        end_time = datetime.now()
        total_time = f"{(end_time - start_time).total_seconds():.2f} seconds"
        with engine.begin() as conn:
            conn.execute(
                text("""
                    UPDATE monitor 
                    SET end_time=:end_time, status=:status, total_time_taken=:total_time 
                    WHERE filename=:filename
                """),
                {"end_time": end_time, "status": f"failed: {str(e)}", "total_time": total_time, "filename": filename_with_timestamp}
            )
        print(f" Error loading {base_filename}: {e}")

# Load all files using threads
def load_all_csvs(folder_path):
    threads = []
    for file in os.listdir(folder_path):
        if file.endswith('.csv'):
            full_path = os.path.join(folder_path, file) 
            table_name = table_map.get(file) 
            if table_name: 
                t = threading.Thread(target=insert_to_db_safe, args=(full_path, table_name))
                threads.append(t)
                t.start()
            else:
                print(f" Skipping '{file}' — No table mapping found.")

    for t in threads:
        t.join()

    print("\n All files processed.\n")

#  Continuous background loader
if __name__ == '__main__':
    folder = r"C:\Users\Nagaraja\Downloads\Training Finsurge-Siva M-Python\Training Finsurge\threadanddb\csv_files"
    while True:
        print(f" Checking folder at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...")
        load_all_csvs(folder) 
        time.sleep(60)  # check again after 60 seconds
