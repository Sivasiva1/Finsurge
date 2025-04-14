from cryptography.fernet import Fernet
import yaml

key = Fernet.generate_key()
cipher = Fernet(key)

password = "Tra!n$pa$$"

encrypted_password = cipher.encrypt(password.encode()).decode()

try:
    with open(r"C:\Users\Nagaraja\Downloads\Training Finsurge-Siva M-Python\Training Finsurge\Encryption\config.yml", "r") as file:
        config = yaml.safe_load(file) or {}  
except FileNotFoundError:
    print("Error: config.yml not found!")
    exit()

config["database"]["password"] = encrypted_password

with open(r"C:\Users\Nagaraja\Downloads\Training Finsurge-Siva M-Python\Training Finsurge\Encryption\config.yml", "w") as file:
    yaml.dump(config, file, default_flow_style=False)

print("Encrypted password updated successfully in config.yml!")
print("Use this key in your main file:", key.decode())
