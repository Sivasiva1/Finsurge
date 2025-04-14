import hashlib, os, base64

# Generate a random salt
salt = os.urandom(16)

def hash_password(password):
    """Hashes a password using PBKDF2."""
    return base64.b64encode(salt + hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)).decode()

def verify_password(password, hashed_password):
    """Verifies a password against a stored hash."""
    decoded = base64.b64decode(hashed_password)
    print(decoded)
    salt, stored_hash = decoded[:16], decoded[16:]
    new_hash = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)
    return new_hash == stored_hash

# Example Usage
password = "mypassword"
hashed_pw = hash_password(password)
print("Hashed Password:", hashed_pw)

# Validate
print("✅ Valid Password!" if verify_password(password, hashed_pw) else "❌ Invalid Password!")
