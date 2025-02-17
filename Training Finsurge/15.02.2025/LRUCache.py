from collections import OrderedDict 
def get(dicti,key=str,value=int):
    if key in dicti:
        print(f"Recently Used {key,value} " ,)
        dicti.move_to_end(key) 
    else:
        print("not in the hashmap") 
def put(dicti,key=str,value=int,capacity=3):
    if len(dicti) >= capacity:
        dicti.popitem(last=False) 
    dicti[key] = value 

dicti = OrderedDict()
put(dicti,"A",1)
put(dicti,"B",2)
put(dicti,"C",3)

get(dicti,"A",1) 

put(dicti,"D",4) 
print(dicti) 