import hashlib 

def withoutsalt(input_password):
    encrypted = hashlib.sha256(input_password.encode()).hexdigest()
    return encrypted 

print("Value 1 :" ,withoutsalt(("siva")))
print("Value 1 :" ,withoutsalt(("siva")))
print("Value 1 :" ,withoutsalt(("siva")))

#Password Validation (Without Salt) 
def validate_password(input_password,hashcode = "229198ac50189365a5dd6412995ab24b4126c777fd69673153f92a0b1ba46882"):
    encrypted = hashlib.sha256(input_password.encode()).hexdigest()
    if encrypted == hashcode:
        return True 
    else:
        return False    
# Simulate user login
print(validate_password("siva")) 
print(validate_password("wrongpassword"))  

