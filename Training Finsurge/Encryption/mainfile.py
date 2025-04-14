import pymysql
import yaml
from cryptography.fernet import Fernet
# Use the encryption key generated earlier 
key = b'8VyRKbAZ2syxM3_awBdkqKv4-kgl-B1tJ6IxoT-Ewvg='
cipher = Fernet(key)

# Load database configuration from YAML
with open(r"C:\Users\Nagaraja\Downloads\Training Finsurge-Siva M-Python\Training Finsurge\Encryption\config.yml", "r") as file:
    config = yaml.safe_load(file)

# Decrypt the password
decrypted_password = cipher.decrypt(config["database"]["password"].encode()).decode()

db = pymysql.connect(
        host=config["database"]["host"],
        user=config["database"]["user"],
        password=decrypted_password,
        database=config["database"]["db_name"]
)
cursor = db.cursor()

cursor.execute("SELECT * FROM emp1")  
rows = cursor.fetchall()

for row in rows:
    print(row)

