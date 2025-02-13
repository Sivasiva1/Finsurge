#comments in python 

#single line comment 
'''multi line comments 
   line 1 
   line 2 
   line 3 
'''

#variables in python 
integer = 5 
string = "hello"
integer_to_float = float(integer)
integer_to_string = str(integer)
print(integer_to_string)
print(integer_to_float)
print(type(integer_to_float),type(integer_to_string))

a = b = c = "hello" #multiple variable with same value 
x, y, z = "Orange", "Banana", "apple" #multiple variable with multiple values 
print(x,y,z)
print(a,b,c)

#global variables 
global_variable = 5 
def function():
    print("this is global variable :",global_variable)
function()

#data types 

#text typen : str 

string = "hello"

#numberical types : int , float , complex 

integr = 199
float_t = 0.9 
comp_t = 1j 

#sequence types : list , tuple , dictionary 
list1 = [1,2] 
tuple = (1,2)
tuple.add(4)

set = {1,2}
set.add(3)
#mapping type 
dicti = {1:3,2:8}
#boolean : true or false 

bool = True 
#memory view type 
yy = 100
print(memoryview(bytes(yy)))

#type casting 
this_is_int = 100 
this_is_str = str(this_is_int)
this_is_str1 = "100"
this_is_int1 = int(this_is_str1)

# 1. Arithmetic Operators
a, b = 10, 3
print("Addition:", a + b)       
print("Subtraction:", a - b)    
print("Multiplication:", a * b)  
print("Division:", a / b)        # 3.333...
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)         
print("Exponentiation:", a ** b) 

# 2. Comparison Operators
print("Equal:", a == b)          
print("Not Equal:", a != b)      
print("Greater than:", a > b)  
print("Less than:", a < b)      
print("Greater or Equal:", a >= b)
print("Less or Equal:", a <= b) 

# 3. Logical Operators
x, y = True, False
print("AND:", x and y)           # False
print("OR:", x or y)             # True
print("NOT:", not x)             # False

# 4. Bitwise Operators
p, q = 5, 3  # 5 = 101, 3 = 011 (binary)
print("Bitwise AND:", p & q)    # 1 (001)
print("Bitwise OR:", p | q)     # 7 (111)
print("Bitwise XOR:", p ^ q)    # 6 (110)
print("Bitwise NOT:", ~p)       # -6

# 5. Assignment Operators
c = 10
c += 5  # c = c + 5 like theat for all arithmetic characters 
print("Assignment Addition:", c)  

# 6. Identity Operators
m, n = [1, 2, 3], [1, 2, 3]
print("Is:", m is n)            # False (different objects)
print("Is Not:", m is not n)    # True

# 7. Membership Operators
lst = [1, 2, 3, 4]
print("In:", 3 in lst)          # True
print("Not In:", 5 not in lst)  # True 

#string operations
text = "Hello"
print(text + " World")  # Concatenation
print(text * 3)  # Repetition
print(len(text))  # String Length
print(text[:3])  # Slicing
print(text.upper())  # Uppercase
print(text.lower())  # Lowercase
print(text.replace("Hello", "Hi"))  # Replacing
print("apple,banana,grape".split(","))  # Splitting
print(" ".join(["Python", "is", "awesome"]))  # Joining
print("Hello" in "Hello World")  # Substring Check

#output formatting 
print("Hello", "World", 123)
print("hi " + "siva")
name = "siva"
age = 22
print(f"My name is {name} and I am {age} years old.")  
for i in range(1,10):
    print(i,end=" ")
print()

#if else
age = 25
voter_id = False
if age > 25 and voter_id:
    print("eligible for voing")
elif age < 25:
    print("not eligible for voting")
elif age>25 and voter_id==False:
    print("not eligible")

#assert instead of try catch 

def division(f,s):
    assert s!=0 , "ZeroDivisionError"
division(10,0)