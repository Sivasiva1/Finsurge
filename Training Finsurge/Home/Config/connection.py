import pymysql
from config_handler import ConfigHandler, logger

class DatabaseConnection:
    def __init__(self):
        try:
            self.config = ConfigHandler().get_database_config()
            if self.config:
                logger.info("Database configuration initialized successfully.")
            else:
                logger.error("Database configuration initialization failed.")
        except Exception as e:
            logger.error(f"Error in database configuration: {e}") 

        self.db = None 
        self.cursor = None 

    def connect(self):
        try:
            self.db = pymysql.connect(
                host=self.config["host"],
                user=self.config["user"],
                password=self.config["password"],
                database=self.config["db_name"]
            )  
            self.cursor = self.db.cursor() 
            logger.info("Database connected successfully.")
        except Exception as e:
            logger.error(f"Database connection failed: {e}")

    def close(self):
        if self.db:
            self.db.close() 
            logger.info("Database connection closed.")

    def fetch_data(self, query):
        try:
            self.cursor.execute(query)
            logger.info(f"Query executed successfully: {query}")
            return self.cursor.fetchall()
        except Exception as e:
            logger.error(f"Failed to execute query: {query} | Error: {e}")
            return None 

    def update_data(self, query):
        try:
            self.cursor.execute(query)
            logger.info(f"Data Updated Successfully: {query}")
        except Exception as e:
            logger.error(f"Failed to execute query: {query} | Error: {e}")
            return None  
