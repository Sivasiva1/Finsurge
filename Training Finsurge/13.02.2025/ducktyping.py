class vechile:
    def move(self):
        return("All vechile is moving ")
 
class car(vechile):
    def move(self):
        return("This car is moving")
    
class bicycle(vechile):
    def move(self):
        return("this is bicycle")# Calls bicycle's move() method (even though it doesn't inherit from vechile)
  
class bii:
    def move(self):
        return("thi")# Calls bicycle's move() method (even though it doesn't inherit from vechile)
d = bii()
print(d.move())
b = bicycle()
c = car()
v = vechile()
print(v.move())
print(c.move())
print(b.move()) #duck typing call 
    