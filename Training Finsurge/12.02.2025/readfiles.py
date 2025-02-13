#read file 
file = open(r"C:\Training Finsurge\12.02.2025\aaa.txt","r")
print(file.read()) 
file.close()

#read file from one folder to another folder 
file = open(r"c:/Training Finsurge/10.2.2025/Cases.py","r")
print(file.read()) 
file.close()

#with ---> no need no close 
with open(r"c:/Training Finsurge/10.2.2025/Cases.py","r") as file:
    print(file.read()) 

#read line by line 
with open(r"c:/Training Finsurge/10.2.2025/Cases.py","r") as file:
    for i in file:
        print(i.strip()) 

#read specific character
with open(r"c:/Training Finsurge/10.2.2025/Cases.py","r") as file:
    print(file.read(10))

#read and write but here no override happens in write
with open(r"C:\Training Finsurge\12.02.2025\bbb.txt", "r+") as file:
    file.write("siva!") #replace the characters 
    file.seek(0)  # Move the pointer back to the start
    print(file.read()) 

#read in binary 

with open(r"C:\Training Finsurge\12.02.2025\bbb.txt","rb") as file:
    print(file.read()) 


#read image in binary mode 
with open(r"C:\Users\ELCOT\Pictures\Screenshots\vi.png","rb") as file:
  print(file.read(10)) 
