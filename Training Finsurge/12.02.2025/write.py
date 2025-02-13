
#write the file (override)
with open(r"C:\Training Finsurge\12.02.2025\aaa.txt","w") as file:
    file.write("hello world")

#write and read 
with open(r"C:\Training Finsurge\12.02.2025\aaa.txt","w+") as file:
   file.write("he")
   file.seek(0)
   print(file.read())

#write in binary 
with open(r"C:\Training Finsurge\12.02.2025\aaa.txt","wb") as file:
    file.write(b"vvv")
#write and read  in binary 

with open(r"C:\Training Finsurge\12.02.2025\aaa.txt","wb+") as file:
    file.write(b"llo")
    file.seek(0)
    print(file.read())