from collections import namedtuple 

nt = namedtuple('Employee',['name','age','salary'])
n1 = nt(("siva","bala"), (20,10), (100,200))
print(n1) 
print(n1.name[0],n1.age,n1.salary) 

#reolace 
n2 = n1._replace(age=20) 
n2 = n1._replace(name="sss")
print(n2)  
#default value 
n3 = namedtuple("Cities",["city","population"],defaults=["Unknown","0"]) 
n3_new = n3("India") 
print(n3_new) 

print(n3_new._fields) 
print(n3_new._asdict()) 
print(n3_new._field_defaults)

print(type(n1))