#positional paramaters 

def addition(name,age):
   print(f" my name is {name} i am {age} years old")
addition("siva",19)
addition(22,"jnoce") # provide output but in wrong order 

#default parameter
def addition(name,age=22):
   print(f" my name is {name} i am {age} years old")
addition("siva") 
addition("siva",70) # it overrides the age 

#keyword parameter
def addition(name,age):
   print(f" my name is {name} i am {age} years old")
addition(age = 90,name = "siva") #position doesnt matter 

#Variable length arguments 

def addition(*args):
   print(sum(args))
addition(1,2,3,4)

def display(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display(name="Shiva", age=21, country="India",salary=10000)

#function scopes 

var = "global" #global scope 

def glob():
  
  var = "enclosing" #enclosing scope 

  def inner():
     var = "local" #local scope 
     print(var)
  inner()
  print(var)

glob()
print(var)

