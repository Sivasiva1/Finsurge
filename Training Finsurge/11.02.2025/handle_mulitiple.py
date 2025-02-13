#using "Exception"

try:
    print(value)
except Exception as e:
    print(e) 
finally:
    print("this is finally block")
#Multiple except Blocks

try:
    print("iquicv"-10)
except TypeError as e:
    print("Type Error:" ,e)
except NameError as e:
    print("Name Error :" ,e) 
except KeyError as e:
    print("KeyError :" ,e)
finally:
    print("This is final block")
#using single except with multiple keyword 
try:
    res = 10/0 
except (ZeroDivisionError,NameError,TypeError) as e:
    print(e)

#try-except-else-finally 
try:
    result = 10 / 10
except Exception as e:
    print(e)
else:
    print(result)
finally:
    print("exceuted successfully")

try:
    print(a) #first error statement is always excecuted in the catch 
    print(5//0) #not considered 
except NameError as e:
    print("NameError:",e)
except ZeroDivisionError as e:
    print(e) 

#raise 
x = 10 
b = 5
if b==0:
    raise ZeroDivisionError("Zero division error")
else:
    print(x/b)