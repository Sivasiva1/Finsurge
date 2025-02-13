class Employee:
    def __init__(self,designation,salary):
        self.designation = designation 
        self.salary = salary 
    def modify(self,d,s):
        self.designation = d 
        self.salary = s 
emp = Employee("intern",10000)
emp.modify("Employee",30000)
print(emp.designation)
print(emp.salary)


class shop:
    def __init__(self,product,price):
        self.product = product
        self.price = price 
    def changeprice(self,rate):
        self.price = rate 
s = shop("banana",10)
print(s.product,s.price)
s.changeprice(20)
print(s.product,s.price)