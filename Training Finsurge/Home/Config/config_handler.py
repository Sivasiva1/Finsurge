import yaml
import logging
import threading
import os
import datetime
from cryptography.fernet import Fernet

LOG_DIR = r"C:\Users\Nagaraja\Downloads\Training Finsurge-Siva M-Python\Training Finsurge\Home\Config\logs"

def setup_logger():
    """Sets up a single logger that logs to both file and console."""
    today = datetime.date.today().strftime("%Y-%m-%d")
    log_folder = os.path.join(LOG_DIR, today)
    os.makedirs(log_folder, exist_ok=True)  # Create date-based folder
    
    log_file = os.path.join(log_folder, "message.log")

    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.DEBUG)  # Change level if needed

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Log format
    log_format = logging.Formatter("%(asctime)s - [%(threadName)s] - %(levelname)s - %(message)s",
                                   "%Y-%m-%d %H:%M:%S")
    file_handler.setFormatter(log_format)
    console_handler.setFormatter(log_format)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Initialize logger
logger = setup_logger()

class ConfigHandler:
    def __init__(self, config_path=r"C:\Users\Nagaraja\Downloads\Training Finsurge-Siva M-Python\Training Finsurge\Home\Config\configuration.yml", 
                 key="P2uN-WOSkUROLBVheq-F_aKawxOI-gG9hbVwQKVIyJ0="):
        self.config_path = config_path
        self.key = key
        try:
            self.config = self.load_config()
            logger.info("Config file loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to load config: {e}")

    def load_config(self):
        with open(self.config_path, "r") as file:
            return yaml.safe_load(file)

    def get_decrypted_password(self):
        try:
            cipher_suite = Fernet(self.key.encode())  
            encrypted_password = self.config["database"]["password"].encode()
            decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
            logger.info("Password decrypted successfully.")
            return decrypted_password
        except Exception as e:
            logger.error(f"Password decryption failed: {e}")
            return None

    def get_database_config(self):
        try:
            db_config = self.config["database"].copy()
            db_config["password"] = self.get_decrypted_password()
            logger.info("Database configuration retrieved successfully.")
            return db_config 
        except Exception as e:
            logger.error(f"Failed to get database config: {e}")
            return None 
