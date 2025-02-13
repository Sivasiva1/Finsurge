'''
syntax error (cant do error handling)
logical error 
common bulit in error 
'''
#logical error 

arr = [10, 20, 30, 40, 50]

print(sum(arr)//len(arr)-1)

#runtime error or common built in error 
#index out bound  
array = [1,2,3]
try:
   print(array[8])
except IndexError as a:
   print(a) 
#assertion error 
try:
   x  = 10 
   assert x >= 12,"x should be grater"
    
except AssertionError as e:
   print("AssertionError",e) 

#attribute error 
try:
   num = "100" 
   num.append(10)
except AttributeError as e:
   print("AttributeError",e)

#import error 
try:
   import aaa 
except ImportError as e:
   print("Import Error :" ,ImportError)

#key error 
try:
   dictinory = {"a":1,"b":2}
   print(dictinory["c"])
except KeyError as e:
   print("Key Error :" ,KeyError)

#Name error 
try:
   print(val)
except NameError as e:
   print("Name Error : " ,e)

#Type error 
try:
   print("vciuewvic"+10)
except TypeError as e:
   print("Type Error :" ,e) 