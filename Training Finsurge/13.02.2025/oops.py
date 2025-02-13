
#class with non - parameter init 
class person:

    def __init__(self):
        self.name = "siva"
        self.age = 100 
obj = person()
print(obj.name)
print(obj.age) 

#class with parameteric init

class employee:
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary
obj1 = employee("siva",100000)
print(obj1.name) 
print(obj1.salary)

#inheritance 
class Parent:
    def display(self):
        print("This is the parent class.")

class Child(Parent):
    def show(self):
        print("This is the child class.")

c = Child()
c.display()  # Inherited from Parent
c.show()     # Child's own method

#multiple inheritance 
class Parent1:
    def method1(self):
        print("Method from Parent1")

class Parent2:
    def method2(self):
        print("Method from Parent2")

class Child(Parent1, Parent2):
    def child_method(self):
        print("Method from Child")

c = Child()
c.method1()
c.method2()
c.child_method()

#multilevel 
class Grandparent:
    def grandparent_method(self):
        print("Grandparent method")

class Parent(Grandparent):
    def parent_method(self):
        print("Parent method")

class Child(Parent):
    def child_method(self):
        print("Child method")

c = Child()
c.grandparent_method()
c.parent_method()
c.child_method()

#heirachical inheritance 
class Parent:
    def parent_method(self):
        print("Parent method")

class Child1(Parent):
    def child1_method(self):
        print("Child1 method")

class Child2(Parent):
    def child2_method(self):
        print("Child2 method")

c1 = Child1()
c1.parent_method()
c1.child1_method()

c2 = Child2()
c2.parent_method()
c2.child2_method()

#polymorphism 
#method overriding 

class poly:
    def hello(self):
        print("hello world")
    
class runtime(poly):
    def hello(self):
        print("hello country")

childobj = runtime()
childobj.hello()
parentobj= poly()
parentobj.hello() 

#method overloading 

class Add():
    def addition(self , a,b,c):
        return a + b + c 
add = Add()
print(add.addition(1,2,3))
print(add.addition(1.1,2.1,4.0))

#abstraction 
from abc import abstractmethod
class abstraction():
    x = 1000 
    @abstractmethod
    def salary(self):
        pass 

    @abstractmethod 
    def employee(self):
        pass
    @abstractmethod 
    def designation(self):
        pass
class child(abstraction):
    def salary(self):
        print (f" Salary is {self.x}")
    def employee(self):
        print("siva")
    def designation(self):
        print("Intern of Finsurge")
obj = child()
obj.salary()
obj.employee()
obj.designation()
  
#super keyword in python 
class p:
    
    def fun(self):
        print("parent")
class c(p):
    def fun(self):
        super().fun() 
o = c()
o.fun() 