import pymysql 
conn = pymysql.connect(
        host="localhost",   
        user="root",
        password="Sivakutty123",
        database="finsurge",
        port=3306  
    )

cursor = conn.cursor()
#insert data 

insert_query = "INSERT INTO Employees VALUES(default,%s,%s,%s,%s)"
data = ("Siva",20,10000,"python")
cursor.execute(insert_query,data)  

# Insert multiple records at once
multiple_data = [
    ("Bob", 25, 55000.00, "IT"),
    ("Charlie", 29, 65000.00, "Finance"),
    ("David", 32, 70000.00, "Sales")
]

cursor.executemany(insert_query,multiple_data) 

conn.commit() 

print("Data Inserted Suceessfully") 