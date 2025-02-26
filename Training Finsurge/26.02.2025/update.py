import pymysql 

conn = pymysql.connect(
    host="localhost",
    user = "root",
    password="Sivakutty123",
    database="finsurge",
    port = 3306
)
cursor = conn.cursor()

update_query = "update employees set salary = 20000 where name = 'siva'"
cursor.execute(update_query) 
conn.commit() 

print("updated sucessfully") 