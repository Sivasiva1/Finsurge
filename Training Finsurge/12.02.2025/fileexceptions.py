try:
    with open("xxx.text","r") as file:
        print(file.read())
except FileNotFoundError as e:
    print(" FileNotFoundError :" , e)

try:
   
    with open(r"C:\Training Finsurge\12.02.2025\new2.txt","xb") as file:
        file.write(b"this is a binary file")
except FileExistsError as e :
    print("FileExistsError ",e)

try:
    with open(r"C:\Training Finsurge\12.02.2025","r") as file:
        print(file.open())
except PermissionError as e:
    print("Permission Error :",e)

