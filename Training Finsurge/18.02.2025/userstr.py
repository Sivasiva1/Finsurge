string = "python"
# Slicing the string
print(string[0:3])  
print(string[2:])   
print(string[:4])   
print(string[::2])  

# Concatenation
str1 = "Hello"
str2 = "World"
greeting = str1 + " " + str2
print(greeting)  

# Repetition
repeat_string = "Python " * 3
print(repeat_string)  

#streing methods 

str = "python is good"

print(str.split(' '))
print(str.upper())
print(str.lower())
print(str.title()) 
print(str.strip())
print(str.startswith("python"))
print(str.endswith("good"))
print(str.replace("is","are"))
