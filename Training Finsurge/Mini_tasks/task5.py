#update while insertion using innner join and temporary table 
import pymysql
import pandas as pd
from sqlalchemy import create_engine
import time

class EmployeeDBManager:
    def __init__(self, csv_path):
        # Database Connection
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
        self.csv_path = csv_path

    def process_data(self):
        start_time = time.time()

        # Step 1: Create Temporary Table
        create_temp_table = """
        CREATE TEMPORARY TABLE IF NOT EXISTS temp_emp AS SELECT * FROM emp WHERE 1=0;
        """
        self.cursor.execute(create_temp_table)
        self.conn.commit()

        # Step 2: Load Data into temp_emp using to_sql
        
        for chunk in pd.read_csv(self.csv_path,chunksize=30):
            chunk.to_sql('temp_emp', con=self.engine, if_exists='append', index=False)

            # Step 3: Update Matching Rows in emp
            update_query = """
            UPDATE emp e
            INNER JOIN temp_emp t ON e.id = t.id AND e.name = t.name AND e.city = t.city
            SET 
                e.age = t.age,
                e.salary = t.salary,
                e.department = t.department,
                e.joining_date = t.joining_date,
                e.performance_score = t.performance_score;
            """
            self.cursor.execute(update_query)
            self.conn.commit()

            # Step 4: Delete Updated Rows from temp_emp
            delete_updated = """
            DELETE t FROM temp_emp t
            INNER JOIN emp e ON t.id = e.id AND t.name = e.name AND t.city = e.city;
            """
            self.cursor.execute(delete_updated)
            self.conn.commit()

            # Step 5: Insert New Rows into emp (if any new data occurs)
            insert_new = """
            INSERT INTO emp (id, name, age, city, salary, department, joining_date, performance_score)
            SELECT id, name, age, city, salary, department, joining_date, performance_score FROM temp_emp;
            """
            self.cursor.execute(insert_new)
            self.conn.commit()

            # Step 6: Clear Temporary Table
            truncate_temp = "TRUNCATE TABLE temp_emp;"
            self.cursor.execute(truncate_temp)
            self.conn.commit()

            end_time = time.time()
            print(f"Inserted/Updated rows using temp table in {end_time - start_time:.2f} seconds")

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        print("DB Connection closed")
