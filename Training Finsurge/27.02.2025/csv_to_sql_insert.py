import pymysql 
import pandas as pd 
from datetime import datetime
conn = pymysql.connect(
        host="localhost",   
        user="root",
        password="Sivakutty123",
        database="messages_db",
        port=3306  
    )

cursor = conn.cursor()
print("-------------connection successful-------------------")
df = pd.read_csv(r"C:\Training Finsurge\27.02.2025\messy_messages.csv")
print(df.head(1)) 

df.drop_duplicates(inplace=True)
df["message_text"] = df["message_text"].fillna("No message") 
df["sender"] = df["sender"].fillna("No Sender")   
df["receiver"] = df["receiver"].fillna("No Receiver")  


def convert_timestamp(date):
        formats = ["%Y-%m-%d %H:%M:%S", "%m/%d/%Y %I:%M %p", "%d-%m-%Y %H:%M:%S"]
        for fmt in formats:
                try:
                    return datetime.strptime(date, fmt).strftime("%Y-%m-%d %H:%M:%S")
                except ValueError:
                    continue
        return None 
df["timestamp"] = df["timestamp"].apply(convert_timestamp) 


def insertion():
# Insert Data into MySQL Table
 for index, row in df.iterrows():
    sql = """
    INSERT INTO messages (message_id, sender, receiver, message_text, timestamp)
    VALUES (%s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE 
    sender=VALUES(sender), receiver=VALUES(receiver), message_text=VALUES(message_text), timestamp=VALUES(timestamp)
    """
    values = (row["message_id"], row["sender"], row["receiver"], row["message_text"], row["timestamp"])
    cursor.execute(sql, values)
    
    conn.commit()
    
    print("Data Inserted Succesfully") 

def deletion():
     
   delete_sql = "DELETE FROM messages WHERE timestamp < NOW() - INTERVAL 30 DAY"
   cursor.execute(delete_sql)
   conn.commit()
   print("----------------data deleted succesfully-----------------")

def updation():
     update_sql = "update messages set sender = 'nobody' where sender = 'No Sender'"
     cursor.execute(update_sql)
     conn.commit()
     print("--------------------data updated succesfully---------------")
def drop():
     drop_sql = "drop table messages"
     cursor.execute(drop_sql)
     conn.commit()
     print("------------------------table dropped succesfully-----------------")
def truncate():
     truncate_sql = "truncate messages"
     cursor.execute(truncate_sql)
     print("------------------------table truncated successfully---------------")
def select():
            
    # Fetch all records
    select_query = "SELECT * FROM messages limit 2"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
while True:
      
      i = str(input("enter the character :\n I : Insertion\n D : Deletion\n U:Updation\n DR: DROP\n T: TRUNCATE\n S: Select\n"))
      if i == "I":
            insertion() 
      elif i == "D":
            deletion()
      elif i == "U":
           updation() 
      elif i == "DR":
           drop()
      elif i == "T":
           truncate() 
      elif i == "S":
            select() 
      else:
            conn.close()
            cursor.close() 
            print("DB Connection closed")
            break 
