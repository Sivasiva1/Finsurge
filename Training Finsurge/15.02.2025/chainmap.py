from collections import ChainMap
#Merging Two Dictionaries
dict1 = {"One":1,"Two":2,"Three":3}
dict2 = {"A":1,"B":2,"C":3}

new = ChainMap(dict1,dict2)
print(new) 
print(new["One"])
print(new["B"]) 

#Updating Values 
new["One"] = 5 
print(new) 

#new_child()

dict3 = {"Name":"Siva","Age":100}
updated = new.new_child(dict3)
print(updated) 

#Using maps to See All Dictionaries 
print(updated.maps) 

#parents removes the first dictionary in the chain. 

print(new.parents) 