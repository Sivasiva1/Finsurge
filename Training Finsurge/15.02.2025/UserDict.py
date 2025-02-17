from collections import UserDict 

class MyDict(UserDict):
    # def __setitem__(self, key, item):
    #     return super().__setitem__(key, item)
    # def __getitem__(self, key):
    #     return super().__getitem__(key)
    pass 
m = MyDict()
m["name"] = "siva"
m["age"] = 100 
# print(m.__getitem__) 
print(m) 

class Mydict2(UserDict):
    def get_keys(self):
         return list(self.keys())

    def remove_keys(self,key):
        if key in self:
            del self[key] 
        else:
            print("not in hash")
    def showvalue(self,key):
        if key in self:
          for k,value in self.items():
            if key == k:
                return value 
        else:
            print("enter the valid key")
    def selectedage(self, value):
        for name, age in zip(self["name"], self["age"]):
            if age == value:
                return name 
        return "Age not found"
m1 = Mydict2()
m1["name"] = ["hello","siva","kutty"]
m1["age"] = [25,20,90]  
print(m1) 

print(m1.get_keys())

print(m1) 
print(m1.showvalue("age")) 
print(m1.selectedage(90))

m1.remove_keys("name") 