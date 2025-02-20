string = "hello world"

string = string.split(' ')
print(string) 

s = "apple,banana,grape"
s = s.split(',')

print(s) 

s = "a b c d" 
s = s.split(" ",2) 
print(s) 

s = "Line1\nLine2\nLine3"
s = s.split("\n")  
print(s) 

import re 

s = "hello world"
s = re.split(" ",s) 
print(s) 

email = "user@example.com"
email = email.split("@") 
print(email[1])  

s = "hello world python"
s = " ".join(s.split(" ")[::-1]) 
print(s) 

s = "document.pdf"
s = s.split('.')[1] 
print(s) 

s = "Welcome to Python programming"
s = s.split(" ")[-1]
print(s) 