#bas e use of lambda 

x  = lambda a : a + 10 

print(x(10))

#lammbda in filter():

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(lambda a : a % 2 == 0 ,list1))) 

# lambda in map()

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(map(lambda a : a**2,list1 )))

#lambda in hashmap 

hashmap = {1:10,2:20,3:30,4:40,5:50}

newhashmap_keyssort= dict(sorted(hashmap.items(),key = lambda a : a[0],reverse=True)) 
newhashmap_valuessort = dict(sorted(hashmap.items(),key=lambda a:a[1],reverse=True))
print(newhashmap_keyssort)
print(newhashmap_valuessort)

#lambda in  pandas 
import pandas as pd 

list1 = [["dhoni",100],["sachin",300],["sachin1",3000]]

df = pd.DataFrame(data = list1 , columns = ["name","age"])

df['uppercase'] = (df['name'].apply(lambda a : a.upper()))

print(df) 
