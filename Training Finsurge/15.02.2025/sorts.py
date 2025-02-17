#1.sorted() 
a = [1,0,3,2,19,-1] 
b = sorted(a)  #creates a new array 
print(b) 

arr = [5, 2, 9, 1, 5, 6]
print(sorted(arr,reverse=True)) #dascending order 

x = ["apple", "banana", "cherry", "date"] 

print(sorted(x,key=len))

dicti = [
    {"name": "Siva", "score": 85},
    {"name": "Bobby", "score": 91},
    {"name": "Ezhil", "score": 78}
]

print(sorted(dicti,key=lambda x:x["score"])) 
print(sorted(dicti,key=lambda x:x["score"],reverse=True)) 

#sort() 

arr1 = [1,2,10,0]
arr1.sort() #modifies the original arr 
print(arr1) 
arr1.sort(reverse=True)
print(arr1) 
print(arr1) 


arr2 =  ["apple", "banana", "cherry", "date"] 
arr2.sort(key=len)
print(arr2) 

arr3  = ["apple", "banana", "kiwi", "cherry"]
arr3.sort(key=lambda x: x[1]) 
print(arr3) 

#all capital letters being sorted before lowercase letters , to avoid this 
#use lower method 

arr4 = ["Aello","World","apple","ant"] 
arr4.sort() #1st capital then small 
print(arr4) 
arr4.sort(key=str.lower) #everything is small 
print(arr4) 

