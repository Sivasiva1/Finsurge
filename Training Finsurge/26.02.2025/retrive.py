import pymysql 
conn = pymysql.connect(
        host="localhost",   
        user="root",
        password="Sivakutty123",
        database="finsurge",
        port=3306  
    )

cursor = conn.cursor()
#select data 

# Fetch all records
select_query = "SELECT * FROM employees where name = 'Siva'"
cursor.execute(select_query)

# Fetch and display data
rows = cursor.fetchall()
print(rows) 
for row in rows:
    print(row)
