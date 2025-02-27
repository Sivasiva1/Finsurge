import pymysql 
import pandas as pd 
from datetime import datetime

class MessageDBManager:
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",   
            user="root",
            password="Sivakutty123",
            database="messages_db",
            port=3306  
        )
        self.cursor = self.conn.cursor()
        print("------------- Connection successful -------------------")
        
        self.df = pd.read_csv(r"C:\Training Finsurge\27.02.2025\messy_messages.csv")
        print(self.df.head(1)) 

        self.df.drop_duplicates(inplace=True)
        self.df["message_text"] = self.df["message_text"].fillna("No message") 
        self.df["sender"] = self.df["sender"].fillna("No Sender")   
        self.df["receiver"] = self.df["receiver"].fillna("No Receiver")  
        self.df["timestamp"] = self.df["timestamp"].apply(self.convert_timestamp) 

    def convert_timestamp(self, date):
        formats = ["%Y-%m-%d %H:%M:%S", "%m/%d/%Y %I:%M %p", "%d-%m-%Y %H:%M:%S"]
        for fmt in formats:
            try:
                return datetime.strptime(date, fmt).strftime("%Y-%m-%d %H:%M:%S")
            except ValueError:
                continue
        return None 

    def insertion(self):
        for _, row in self.df.iterrows():
            sql = """
            INSERT INTO messages (message_id, sender, receiver, message_text, timestamp)
            VALUES (%s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
            sender=VALUES(sender), receiver=VALUES(receiver), message_text=VALUES(message_text), timestamp=VALUES(timestamp)
            """
            values = (row["message_id"], row["sender"], row["receiver"], row["message_text"], row["timestamp"])
            self.cursor.execute(sql, values)
            self.conn.commit()
        print("Data Inserted Successfully") 

    def deletion(self):
        delete_sql = "DELETE FROM messages WHERE timestamp < NOW() - INTERVAL 30 DAY"
        self.cursor.execute(delete_sql)
        self.conn.commit()
        print("---------------- Data deleted successfully -----------------")

    def updation(self):
        update_sql = "UPDATE messages SET sender = 'nobody' WHERE sender = 'No Sender'"
        self.cursor.execute(update_sql)
        self.conn.commit()
        print("-------------------- Data updated successfully ---------------")

    def drop(self):
        drop_sql = "DROP TABLE messages"
        self.cursor.execute(drop_sql)
        self.conn.commit()
        print("------------------------ Table dropped successfully -----------------")

    def truncate(self):
        truncate_sql = "TRUNCATE TABLE messages"
        self.cursor.execute(truncate_sql)
        self.conn.commit()
        print("------------------------ Table truncated successfully ---------------")

    def select(self):
        select_query = "SELECT * FROM messages LIMIT 2"
        self.cursor.execute(select_query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        print("DB Connection closed")

if __name__ == "__main__":
    db_manager = MessageDBManager()
    while True:
        i = input("Enter the character:\n I : Insertion\n D : Deletion\n U: Updation\n DR: DROP\n T: TRUNCATE\n S: Select\n")
        if i == "I":
            db_manager.insertion()
        elif i == "D":
            db_manager.deletion()
        elif i == "U":
            db_manager.updation()
        elif i == "DR":
            db_manager.drop()
        elif i == "T":
            db_manager.truncate()
        elif i == "S":
            db_manager.select()
        else:
            db_manager.close_connection()
            break
