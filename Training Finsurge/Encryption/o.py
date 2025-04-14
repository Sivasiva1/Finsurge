from mainfile import  db,cursor

cursor.execute("SELECT * FROM emp1")
rows = cursor.fetchall()

for row in rows:
    print(row)

db.close()
