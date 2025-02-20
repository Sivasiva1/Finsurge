list1 = [1,2,3,4]
new = frozenset(list1)
print(new) 

# new[0] = 1
# print(new) 


set1 = (1,2,3)
newset = frozenset(set1)
print(newset) 

# newset[0] = 10 
# print(newset) 

dict1 = {1:2 , 2:3}
newdictall = frozenset(dict1.items())
newdictkeys = frozenset(dict1.keys())
print(newdictall) 
print(newdictkeys) 

# newdictall[1]=10 


#allows set operations 
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

print(fs1 | fs2)  
print(fs1 & fs2)  
print(fs1 - fs2) 

#immutable  
fs = frozenset([10,10,10])
try: 
    fs.add(20) 
except Exception as e:
    print(e) 

#membership 
print(10 in fs)
print(20 in fs)

a = set([10,10,10])
a.add(20) 

#use as a dictionary key 
data = {
    frozenset(["apple", "banana"]): "Fruits",
    frozenset(["carrot", "spinach"]): "Vegetables"
}

print(data[frozenset(["apple", "banana"])])  

#remove duplicates in list of lists 
lists = [[1, 2, 3], [3,2,1], [4, 5, 6], [1, 2, 3]]
u = set()

# for i in lists:
#     u.add(i)
# print(u) 


for i in lists:
    u.add(frozenset(i))
print(u)