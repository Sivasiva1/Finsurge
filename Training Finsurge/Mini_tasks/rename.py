import pymysql
import time
from sqlalchemy import create_engine 
import pandas as pd 
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="Sivakutty123",
    database="dummy",
    port=3306
)
cursor = conn.cursor()
print("------------- Connection successful -------------------")
csv = "C:\Training Finsurge\OS_CSV\employee_data_cleaned.csv"
engine = create_engine("mysql+pymysql://root:Sivakutty123@localhost/dummy")
  
# temp : new_emp , main:emp 
#1 . create a temp table 

create_temp = "create table new_emp like emp;" 
cursor.execute(create_temp) 
conn.commit()

#2. insert to temp using chunk 
start = time.time()
for chunk in pd.read_csv(csv,chunksize=1000):
    chunk.to_sql("new_emp",con=engine,if_exists = "append",index = False) 
end = time.time()
print(f"time taken for inserting data to temporary table {end-start:.6f} seconds") 
conn.commit() 

#3. drop main table 
start = time.time()
drop_sql = "drop table emp"
cursor.execute(drop_sql) 
end = time.time() 
print(f"time taken for drop main table {end-start:.6f} seconds") 
conn.commit()

#4 . rename the temp as main 
start = time.time()
rename_sql = "rename table new_emp to emp"  
cursor.execute(rename_sql) 
end = time.time() 
print(f"time taken for rename temp to main table {end-start:.6f} seconds") 

conn.commit()

cursor.close()
conn.close() 