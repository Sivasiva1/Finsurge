#new style class
#multiple inheritence 
class A:
    def fun(self):
        print("this is 1st parent")
    
class B:
    def fun(self):
        print("this is 2nd parent")
    
class C(A,B):
   pass

c = C()
c.fun()
    
#MethodResolutionOrder: C -- > A --- > B

#supports super()

class Animal:
    def face(self):
        print("face is terrified")
class Dog(Animal):
    def face(self):
        super().face()

dog = Dog()
dog.face()

#@property - getter , @attribute.setter 

class Employee:
    def __init__(self,name):
      self.__name = name #private attribute 
    
    @property
    def _name(self):
        return self.__name

    @_name.setter
    def _name(self, value):
        self.__name = value

