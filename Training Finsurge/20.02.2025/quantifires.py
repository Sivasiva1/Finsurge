import re 

#Check if a string has consecutive digits 
string  = "hello 432 111"
digits = (re.findall(r"\d+",string))
print(digits) 


s = "beautiful tree" 
vowel = re.findall(r"[aeiouAEIOU]+",s) 
print(vowel)  

s = "9876543210" 
istrue = bool(re.fullmatch(r"\d{10}",s)) 
print(istrue) 

s = "Trending #Python #Coding" 

hash = re.findall(r"#w+",s)
print(hash) 

text = "Order 123, not 123abc!"
match = re.findall(r"\b123\b", text)
print(match)     #boundary can be " ",.,!,",",""

s = "contact me at sachinsiva231@example.com"

mail = re.findall(r"\b[a-zA-Z0-9]+@[a-zA-Z0-9]+\.\w{2,}\b",s) 
print(mail) 