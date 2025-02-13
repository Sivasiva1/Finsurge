with open(r"C:\Training Finsurge\12.02.2025\new.txt","x+") as file:
    file.write("this is a new file ")
    file.seek(0)
    print(file.read())

with open(r"C:\Training Finsurge\12.02.2025\new2.txt","xb") as file:
     file.write(b"this is a binary file")

with open(r"C:\Training Finsurge\12.02.2025\new3.txt","xb+") as file:
     file.write(b"this is create,read and write binary file")
     file.seek(0)
     print(file.read())

