import pymysql
import pandas as pd
import time

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
       
        print("------------- Connection successful -------------------")

        self.csv_path = csv_path 
    def insert_ignore_then_update(self):
        start_time = time.time()
        
        # Load CSV into DataFrame
        df = pd.read_csv(self.csv_path)
        values = df.values.tolist()

        # Insert IGNORE
        insert_sql = """INSERT IGNORE INTO emp (id, name, age, city, salary, department, joining_date, performance_score) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        self.cursor.executemany(insert_sql, values)
        self.conn.commit()

        inserted_rows = self.cursor.rowcount  # Get number of rows inserted

        # Update existing rows
        update_sql = """UPDATE emp 
                        SET age = %s, salary = %s, department = %s, joining_date = %s, performance_score = %s
                        WHERE id = %s AND name = %s AND city = %s"""
        update_values = [(row[2], row[4], row[5], row[6], row[7], row[0], row[1], row[3]) for row in values]
        self.cursor.executemany(update_sql, update_values)
        self.conn.commit()

        updated_rows = self.cursor.rowcount  # Get number of rows updated

        end_time = time.time()

        print(f"Rows inserted: {inserted_rows}")
        print(f"Rows updated: {updated_rows}")
        
        print(f"Time taken: {end_time - start_time:.2f} seconds")

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        print("DB Connection closed")
