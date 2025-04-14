import threading
from connection import DatabaseConnection
from config_handler import logger

def main():
    logger.info("Thread Started Successfully")
    
    db_conn = DatabaseConnection()
    db_conn.connect()

    query = "SELECT * FROM emp1" 
    query2 = "UPDATE emp1 SET NAME = 'SACHIN' WHERE ID = 1" 
    rows = db_conn.fetch_data(query)

    if rows:
        for row in rows:
            print(row)
    else:
        print("No data retrieved.")

    db_conn.update_data(query2) 
    db_conn.close()

if __name__ == "__main__":
    thread = threading.Thread(target=main, name="DBThread")
    thread.start() 
    thread.join() 
    logger.info("Thread Ended Successfully")
