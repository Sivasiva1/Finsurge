#Using an Iterator
l  = [10,20,20,40]
l1 = iter(l)

print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1)) 

#while loop 
list1 = [1,2,3,4] #iteratable 
l2 = iter(list1) 
while True:
    try:
        print(next(l2))
    except StopIteration:
        break 


