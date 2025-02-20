#Handling Special Characters
import re 
text = "Hello! Are you #ready gdiugui3475@*^*^@"
print(re.findall(r"[!@#$%]",text)) 

text = "Hello@World! #Python123" 
print(re.sub(r"[!@#$%&]","",text))

#email validation abnd email extraction 

email = "hello world sachinsiva231@gmail.com"
answer = "".join(re.findall(r"\b[A-Za-z0-9]+@[A-Za-z]+\.[a-z]{2,}\b",email)) 
 
print("Email :",answer) 

pattern = r"\b[A-Za-z0-9]+@[A-Za-z]+\.[a-z]{2,}\b" 
emails = [
    "example123@gmail.com",
    "user.name@domain.co.in",
    "invalid-email@.com",
    "user@domain123.org"
]
for i in emails :
    if re.match(pattern,i): 
        print("true")
    else:
        print("false") 
        
#date extracting 
date = "12-12-2023"

date_format = re.findall(r"^(0[1-9]|1[0-9]|2[0-9]|3[0-1])-(0[1-9]|1[0-2])-(\d{4})$",date)  

print("DATE FORMAT :",date_format)
print("DAY : " ,date_format[0][0]) 
print("MONTH :",date_format[0][1])  
print("YEAR :",date_format[0][2])   

