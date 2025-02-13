with open(r"C:\Training Finsurge\12.02.2025\ccc.txt","a") as file:
    file.write("how")
    file.write(" are you ")

#append and read 
with open(r"C:\Training Finsurge\12.02.2025\ccc.txt","a+") as file:
    file.write(" hello ")
    file.seek(0)
    print(file.read())

#append in binary 
with open(r"C:\Training Finsurge\12.02.2025\ccc.txt","ab") as file:
    file.write(b"siva")

#append , read in binary 

with open(r"C:\Training Finsurge\12.02.2025\ccc.txt","ab+") as file:
    file.write(b" m ")
    file.seek(0)
    print(file.read())
