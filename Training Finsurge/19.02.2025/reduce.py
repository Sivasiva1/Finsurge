#reduce always return a single value or single itearable 
#only take two arguments 
from functools import reduce 
arr = [1,2,3]
def add(x,y):
    return x + y 
ans = reduce(add,arr)
print(ans) 

numbers = [12, 45, 67, 23, 89, 34] 
def maxi(x,y):
     return x if x > y else y 
res = reduce(maxi,numbers) 
print(res) 

words = ["Hello", " ", "World", "!"] 

con = reduce(lambda x,y : x + y , words)
print(con) 

numbers = [1, 2, 3, 4, 5] 
prod = reduce(lambda x,y : x * y,numbers)
print(prod) 

n = 5 
fact = reduce(lambda x,y:x*y ,range(1,n+1)) 

number = [48, 36, 60, 72]
import math 
gcd = reduce(lambda x,y:math.gcd(x,y),number) 
print(gcd) 

data = ['a', 'b', 'a', 'c', 'b', 'a', 'b']
def freq(dicti,value):
    
        if value not in dicti:
            dicti[value] = 1 
        else:
            dicti[value]+=1 
        return dicti 
count = reduce(freq,data,{}) 
print(count) 

numbers = [1, 2, 2, 3, 4, 4, 5] 

def finddup(array,daata): #array : iterables always in left , iterable value daata in right 
    
     if daata not in array:
        array.append(daata) 
     return array  
dupli = reduce(finddup,numbers,[]) 
print(dupli)  
