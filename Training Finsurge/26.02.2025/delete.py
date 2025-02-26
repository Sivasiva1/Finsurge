import pymysql 

conn = pymysql.connect(
    host="localhost",
    user = "root",
    password="Sivakutty123",
    database="finsurge",
    port = 3306
)
cursor = conn.cursor()

delete_query = "delete from employees where name = 'siva'"

cursor.execute(delete_query)

conn.commit() 

print("rows deleted successfully")

cursor.close() 
conn.close()
