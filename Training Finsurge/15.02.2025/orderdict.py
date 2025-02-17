from collections import OrderedDict 

o = OrderedDict()
o["Name"] = "siva"
o["Designation"] = "Intern"
o["Age"] = 21 

print(o) 

#Comparing dict and OrderedDict

dict1 = {'b': 1, 'a': 2, 'c': 3}
dict2 = OrderedDict({'b': 1, 'a': 2, 'c': 3})

print(dict1 is dict2)  # True (insertion order is maintained)

#OrderedDict is still useful for reordering elements.

dict2.move_to_end("b") 
print(dict2) 
dict2.move_to_end("b",last=False) 
print(dict2) 

reverse = OrderedDict(reversed(dict2.items())) 
print(reverse) 
