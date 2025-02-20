import re 
#remove number
text = "My number is 12345."

print(re.sub(r"[0-9]","*",text)) 

text = "Hello     world!   Python    is  great."

print(re.sub(r"[\s]+"," ",text))

#remove numbers 
text = "Hello123, today is 2025!" 

print(re.sub(r"[\d]","",text)) 

#remove special charcaters 
text = "Hello@World! Python#Regex." 
print(re.sub(r"[\W]","",text)) 

#replace a word sarts with 
text = "Hello world, welcome to Python!" 
print(re.sub(r"^Hello","Hi",text))


#replace domain 
email = "user123@gmail.com"
new_email = re.sub("@gmail", "@yahoo", email)
print(new_email)

text = "Hello123, Python! @Regex 2025" 
print(re.sub(r"[^a-zA-z\s]","",text))


#search()
pattern = r"World!"
string = "Hello, World!"
search = re.search(pattern,string)
print(search.group())
