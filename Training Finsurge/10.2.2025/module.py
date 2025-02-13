import basemodule as bs
from basemodule import employee 

'''if we run this module base module runs automatically except the main 
block because this module import the base module'''
bs.calculator(num1=10,num2=5)

#dir(): show all the functions availabe in basemodule class 

class M:
    pass 
print(dir(bs))

#speciflily access
print(employee["name"]) 
print(employee["Desingantion"])

#example for __doc__ 
print(bs.calculator.__doc__)
print(__name__)# '__main__' if run directly
print(bs.__name__)  

print(bs.C.__module__)
print(M.__module__) 