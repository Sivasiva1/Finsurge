dicti = [
    {"name": "Siva", "score": 85},
    {"name": "Bobby", "score": 91},
    {"name": "Ezhil", "score": 78}
] 
# print(sorted(dicti,key=lambda x:x["score"])) 
# print(sorted(dicti,key=lambda x:x["score"],reverse=True)) 
try:
    print(sorted(dicti)) 
except Exception as e:
    print("Error Occured :",e)

l1 = [100,2000,20000]

try:
    print(sorted(l1,key=len))
except Exception as e:
    print("Error Occured :",e) 