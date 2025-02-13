try:
    with open("xxx.text","r") as file:
        print(file.read())
except Exception as e:
    print( e)


try:
    with open("xxx.text","r") as file:
        print(file.read())
except FileExistsError as e:
    print(e)
except FileExistsError as e:
    print(e)
except IOError as e:
    print(e)
except PermissionError as e:
    print(e)

try:
    with open(r"C:\Training Finsurge\12.02.2025\new2.txt","xb") as file:
        file.write(b"this is a binary file")
except (FileExistsError,FileNotFoundError,PermissionError) as e :
    print(e) 