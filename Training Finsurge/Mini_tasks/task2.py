'''Task Name : i ) Inserting bulk dataframe 
                ii) update row if id,city,name are same , else insert 
                using on duplicate key update (best approach for mysql)'''
import pymysql
import pandas as pd
import time
import sys

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

        self.csv_path = csv_path  # Save CSV file path for chunked reading

    def insert_using_executemany(self):
        start_time = time.time()
        
        sql = """INSERT INTO emp (id, name, age, city, salary, department, joining_date, performance_score) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s) 
                ON DUPLICATE KEY UPDATE 
                age = VALUES(age),
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
    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        print("DB Connection closed")

# if __name__ == "__main__":
#     if len(sys.argv) == 1:
#         print("No Path Given")
#         sys.exit(1)

#     csv_file_path = sys.argv[1]  # Read CSV file path from the command line
#     db_manager = EmployeeDBManager(csv_file_path)

#     Input = str(input("Enter the input (executemany, tosql, close): "))
#     while True:
#         if Input == "executemany":
#             db_manager.insert_using_executemany()
#             break
       
#         elif Input == "close":
#             db_manager.close_connection()
#             break
