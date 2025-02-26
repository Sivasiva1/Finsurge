import pymysql


conn = pymysql.connect(
        host="localhost",   
        user="root",
        password="Sivakutty123",
        database="finsurge",
        port=3306  
    )

cursor = conn.cursor()
print("Connected to MySQL successfully!")

# Create table query
create_table_query = """
    CREATE TABLE IF NOT EXISTS Employees (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(100) NOT NULL,
        Age INT,
        Salary DECIMAL(10, 2),
        Department VARCHAR(50)
    );
    """

cursor.execute(create_table_query)
print("Table 'Employees' created successfully!")

