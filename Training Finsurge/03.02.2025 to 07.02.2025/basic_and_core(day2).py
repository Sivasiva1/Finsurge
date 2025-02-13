#for loop 

for i in range(1,10):
    print(i,end=" ")
print()

#while loop
i = 0 
while i<10:
    print(i,end=" ")
    i+=1 
print()

#function 

def findeven(array):
    evenarray = []
    for i in a:
        if i % 2==0:
          evenarray.append(i)
    return evenarray 
a = [1,2,3,4]
print(findeven(a)) 

#list comprehension 

array = [1,2,3,4]

list1 = [i**2 for i in array if i%2==0]
print(list1) 

#dictinory comprehension 

dict1 = {i : i**2 for i in array if i % 2==0}
print(dict1)

#lamdba function 

x = lambda a : a + 5 
print(x(5)) 

#break and continue 

for i in range(10):
    if i == 5:
        break 
    elif i == 1:
        continue 
    else:
        print(i) 

#list operations 

l = [10,20,30,40]

l.append(50) #push 
print(l.pop()) #pop 
print(l[-1]) #peek 
print(l[::-1]) #reverse 
l.remove(10) #remove element 
print(l) 

#try except 
varaiable= 1
try:
    print(u) 
except NameError:
    print("a is not assigned")
finally:
    print("this is a finally block")

#hashmap 

hash = {}

countarray = [1,21,1,2,2]

for i in countarray:
    if i in hash:
        hash[i]+=1 
    else:
        hash[i]=1 
print(hash)
print(hash.keys())
print(hash.values())
sortedkeys = dict(sorted(hash.items(),key = lambda a : a[0])) # sorting hashmap based on the keys in asc 
sortedValues = dict(sorted(hash.items(), key=lambda a:a[1])) #sorting hashmap based on the keys in asc 

sortedkeysdesc = dict(sorted(hash.items(),key = lambda a : a[0],reverse=True)) # sorting hashmap based on the keys in desc
sortedValuesdesc = dict(sorted(hash.items(), key=lambda a:a[1],reverse=True)) #sorting hashmap based on the keys in desc 

print(sortedkeys)
print(sortedValues)
print(sortedkeysdesc)
print(sortedValuesdesc) 

#mutables 

list2 = [1,2,3,4]
list2[2]=100 
print(list2)

myset = {"apple", "banana", "cherry"}
myset.add("hello") 
print(myset) 

#immutables 
string = "hello world"
print(reversed(string))

'''tuple = (1,2,3,4)
tuple[0] =200
print(tuple)
''' 

#zip() function in python 

zip1 = [1,2,3]
zip2 = ["one","two","three"]

zipped = zip(zip1,zip2)
print(list(zipped))  