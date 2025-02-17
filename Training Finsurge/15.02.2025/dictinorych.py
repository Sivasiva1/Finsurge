dicti = {x:x**2 for x in range(5)}
print(dicti) 
d = {i:i*i for i in range(10)if i % 2==0}
print(d) 
keys = ["siva","naga","mani","bala"]
value=[10,20,30,40]
kvd = {k:v for k,v in zip(keys,value)}
print(kvd)

original = {'a': 1, 'b': 2, 'c': 3} 
swapp = {v:k for k,v in original.items()}
print(swapp) 

words = ["hello",'world',"cinema","cricket","thriller"]
cond = {len(i):i for i in words if len(i)>=5}
print(cond) 

matrix = {i:{j: i*j for j in range(1,5)} for i in range(1,5)}
print(matrix) 

txt = "dictionary"
count = {i:txt.count(i) for i in txt }
print(count) 

default = {i:0 for i in keys}
print(default) 

vowelstr ="hello my name is siva"
v= {i:vowelstr.count(i) for i in vowelstr if i in "aeiouAEIOU"}
print(v) 