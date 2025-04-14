import hashlib
'''Without Salt'''
data = "HelloWorld".encode()
# hashlib - MD5
md5_hash = hashlib.md5(data).hexdigest()
print("MD5 Hash:", md5_hash)

#hashlib - SHA256
sha256_hash = hashlib.sha256(data).hexdigest()
print("SHA256 Hash:", sha256_hash)

'''With Salt'''
import base64
#base64 
encoded = base64.b64encode(data)
print("Base64 Encoded:", encoded)

import os
#pbkdf2
salt = os.urandom(16)  

hashed_password = hashlib.pbkdf2_hmac("sha256", data, salt, 100000)
print("PBKDF2HMAC Hash:", hashed_password.hex())

import bcrypt
#bcrypt 
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(data, salt)

print("Bcrypt Hashed Password:", hashed_password)





