from Crypto.Cipher import AES
import base64

def pad(data):
    return data + (16 - len(data) % 16) * chr(16 - len(data) % 16)

def unpad(data):
    return data[:-ord(data[-1])]

# Key and IV (both must be 16, 24, or 32 bytes long)
key = b'Sixteen byte key'
iv = b'RandomInitVectos' 

def encrypt(data):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_bytes = cipher.encrypt(pad(data).encode())
    return base64.b64encode(encrypted_bytes).decode()

def decrypt(encrypted_data):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = cipher.decrypt(base64.b64decode(encrypted_data))
    return unpad(decrypted_bytes.decode())

message = "Hello, AES encryption! Done"
encrypted_message = encrypt(message)
decrypted_message = decrypt(encrypted_message)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
