import pymysql
import time
from sqlalchemy import create_engine
import pandas as pd

# Database connection
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="Sivakutty123",
    database="dummy",
    port=3306
)
cursor = conn.cursor()
print("------------- Connection successful -------------------")

csv = r"C:\Training Finsurge\OS_CSV\employee_data_cleaned.csv"
engine = create_engine("mysql+pymysql://root:Sivakutty123@localhost/dummy")

# Step 1: Create a new table (temp table)
create_temp = "CREATE TABLE IF NOT EXISTS new_emp LIKE emp;"
cursor.execute(create_temp)
conn.commit()

# Step 2: Insert into temp table using chunks
start = time.time()
for chunk in pd.read_csv(csv, chunksize=1000):
    chunk.to_sql("new_emp", con=engine, if_exists="append", index=False)
end = time.time()
print(f"Time taken for inserting data into temp table: {end - start:.6f} seconds")

conn.commit()

# Step 3: Create or Replace a View pointing to new_emp
start = time.time()
create_view = "CREATE OR REPLACE VIEW emp_view AS SELECT * FROM new_emp;"
cursor.execute(create_view)
end = time.time()
print(f"Time taken for creating/updating the view: {end - start:.6f} seconds")

conn.commit()

# Closing the connection
cursor.close()
conn.close()
print("DB Connection closed.")
