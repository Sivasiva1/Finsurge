import hashlib
import os
import base64

# Hash password WITH salt (different output each time)
def withsalt(input_password):
    salt = os.urandom(16)  # Generate a random 16-byte salt
    hashed = hashlib.pbkdf2_hmac('sha256', input_password.encode(), salt, 100000)
    return base64.b64encode(salt + hashed).decode()  # Store salt + hash

# Print different hashes for the same password
print("Value 1 :", withsalt("siva"))
print("Value 2 :", withsalt("siva"))
print("Value 3 :", withsalt("siva"))

# Password Validation (With Salt)
def validate_password_with_salt(input_password, stored_hash):
    data = base64.b64decode(stored_hash)
    salt = data[:16]  # Extract salt
    stored_hashed = data[16:]  # Extract stored hash
    # Recompute the hash with the provided input password and extracted salt
    new_hashed = hashlib.pbkdf2_hmac('sha256', input_password.encode(), salt, 100000)
    return new_hashed == stored_hashed

stored_hash = withsalt("siva")
print(stored_hash)
# Simulate user login
print("\nValidation 1 (Correct Password):", validate_password_with_salt("siva", stored_hash))  
print("Validation 2 (Wrong Password):", validate_password_with_salt("wrongpassword", stored_hash)) 