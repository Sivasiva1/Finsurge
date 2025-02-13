import math

result = math.sqrt(25)
print("Square root of 25:", result)

result = math.factorial(5)
print("Factorial of 5:", result)

result = math.pow(2, 3)
print("2 raised to the power of 3:", result)

radius = 7
area = math.pi * radius ** 2
print("Area of the circle with radius 7:", area)

import datetime

# 1. Current Date and Time
current_datetime = datetime.datetime.now()
print("Current Date and Time:", current_datetime)

# 2. Current Date
current_date = current_datetime.date()
print("Current Date:", current_date)

# 3. Current Time
current_time = current_datetime.time()
print("Current Time:", current_time)

#4.Current Year 
print("Current Year :",current_date.year)

#5.current Month 
print("Current Month :",current_date.month)

#6.current day
print("Current Dday :",current_date.day)


import re 

#match()
s1 = r"^hello"
s2 = "hello world"
match = re.match(s1,s2)
print(match.group())

#search()
pattern = r"World!"
string = "Hello, World!"
search = re.search(pattern,string)
print(search.group)

#sub()
digit = r"\d"
number = "My phone no 1234567"
new = re.sub(digit,"@",number)
print(new)
import os 

print("Current Directory :" , os.getcwd())
print("List all contents in directory :",os.listdir())
'''print("Creation of new directory :",os.mkdir("new_folder"))
print(os.rmdir("new_folder"))
os.rename("hii","hello")'''
import webbrowser 
webbrowser.open("https://www.python.org")

import random
# Generate a random number between 1 and 100
print(random.randint(1, 100))

import sys 
#sys module 

print("Python version ",sys.version)
print("Directory full path ",sys.argv)
sys.exit()
print("iubeuie2gueo")

