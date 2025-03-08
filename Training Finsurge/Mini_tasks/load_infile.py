import pymysql
import time

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="Sivakutty123",
    database="dummy",
    port=3306
)
cursor = conn.cursor()
print("------------- Connection successful -------------------")

#  delete time
start_time = time.time()
cursor.execute("DELETE FROM temp_emp")
conn.commit()
delete_time = time.time() - start_time
print(f"Time taken to delete records: {delete_time:.6f} seconds")

query = """
LOAD DATA INFILE 'C:/MySQLUploads/employee_data_cleaned.csv'
INTO TABLE temp_emp
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
"""

#  load time
start_time = time.time()
cursor.execute(query)
conn.commit()
load_time = time.time() - start_time
print(f"Time taken to load records: {load_time:.6f} seconds")

cursor.close()
conn.close()
