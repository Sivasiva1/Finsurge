#ATM Scernerio using while loop 

amount = 100
balance = 1000

while balance >= amount:
    
    
    print("current balance ",balance)
    print("Withdrawl Succesul")
    balance-=amount 
    
    if balance < amount:
        print(f"{balance } Insufficient Balance")
        break 
    else:
        continue 
#while loop 
count = 10
i=3 
while i < count:
    if i % 2 ==0:
        print("divisible by 2 :" , i,end=" ")
    
    elif i % 3==0:
        print("divisible by 3 :",i,end=" ")
  
    elif i % 4 ==0:
        continue
 
    elif i % 5==0:
        print("divisible by 5: ",i,end=" ")
    else:
        break 
    i+=1 
print()
#reverse only vowels 

string = "helloworld"
string = list(string)
left = 0 
right = len(string)-1 
vowels = "aeiouAEIOU"
while left < right:

    while left < right and string[left] not in vowels:
        left+=1 
    while left<right and string[right] not in vowels:
        right-=1
    
    if left<right:
        temp = string[left]
        string[left] = string[right]
        string[right] = temp 
        left+=1
        right-=1 
print(string) 

while True:
   value = int(input("Enter the value"))
   if value < 30:
       break 


   
   