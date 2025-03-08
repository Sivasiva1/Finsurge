'''Task Name : i ) Iserting bulk dataframe using execuute,executemany , 
                tosql and measuring execution time and memory 
                ii) Take csv path as a command line argument using sys 
                ii) update while inserting if id is same (key column : id)'''

import pymysql
import pandas as pd
import time
from sqlalchemy import create_engine
import sys
from memory_profiler import profile

class EmployeeDBManager:
    def __init__(self, csv_path):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password="Sivakutty123",
            database="dummy",
            port=3306
        )
        self.cursor = self.conn.cursor()
        self.engine = create_engine("mysql+pymysql://root:Sivakutty123@localhost/dummy")
        print("------------- Connection successful -------------------")

        self.csv_path = csv_path  # Save CSV file path for chunked reading

    def insert_using_execute(self):
        start_time = time.time()
        sql = """INSERT INTO employees (id, name, age, city, salary, department, joining_date, performance_score) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE
                      name = VALUES(name),
                age = VALUES(age),
                city = VALUES(city),
                salary = VALUES(salary),
                department = VALUES(department),
                performance_score = VALUES(performance_score)"""
        for chunk in pd.read_csv(self.csv_path, chunksize=1000):  # Read in chunks
            
            for _, row in chunk.iterrows():
                self.cursor.execute(sql, tuple(row))
            self.conn.commit()
        end_time = time.time()
        print(f"Inserted rows using `execute()` in {end_time - start_time:.2f} seconds")

    
    @profile
    def insert_using_executemany(self):
        start_time = time.time()
        
        sql = """INSERT INTO employees (id, name, age, city, salary, department, joining_date, performance_score) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s) 
                ON DUPLICATE KEY UPDATE 
                name = VALUES(name),
                age = VALUES(age),
                city = VALUES(city),
                salary = VALUES(salary),
                department = VALUES(department),
                joining_date = VALUES(joining_date),
                performance_score = VALUES(performance_score)"""

        for chunk in pd.read_csv(self.csv_path, chunksize=1000):
            chunk['id'] = chunk['id'].astype(int)  # Ensure `id` is integer
            values = chunk.values.tolist()
            self.cursor.executemany(sql, values)
            self.conn.commit()

        end_time = time.time()
        print(f"Inserted/Updated rows using `executemany()` in {end_time - start_time:.2f} seconds")

    def insert_using_to_sql(self):
        start_time = time.time()
        for chunk in pd.read_csv(self.csv_path, chunksize=1000):
            chunk.to_sql('employees', con=self.engine, if_exists='append', index=False)
        end_time = time.time()
        print(f"Inserted rows using `to_sql()` in {end_time - start_time:.2f} seconds")

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        print("DB Connection closed")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No Path Given")
        sys.exit(1)

    csv_file_path = sys.argv[1]  # Read CSV file path from the command line
    db_manager = EmployeeDBManager(csv_file_path)

    Input = str(input("Enter the input (execute, executemany, tosql, close): "))
    while True:
        if Input == "execute":
            db_manager.insert_using_execute()
            break
        elif Input == "executemany":
            db_manager.insert_using_executemany()
            break
        elif Input == "tosql":
            db_manager.insert_using_to_sql()
            break
        elif Input == "close":
            db_manager.close_connection()
            break

