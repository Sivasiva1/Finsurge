def decorator(callingbase):
    def w(): #wrap the function to delays the execution 
        print("before calling the base")
        callingbase() 
    return w
@decorator #short hand : base = decorator(base) 
def base():
    print("base function") 

base() 

#execution time using decorator 
import time 

def timer(bases):
    def wrapper():
        st = time.time()
        bases()
        et = time.time()
        print(f"execution time {et-st:.5f}")
    return wrapper 

@timer 
def bases():
    print("hello")
bases() 


def authenctication(basess):
    def wrapper(username,password):
       
        if username == "siva" and password == "password123":
            print("All set !!!")
            basess()
        else:
            print("wrong details..........")
    return wrapper 

@authenctication 
def basess():
    print("Welcome to the website")


basess("siva","password123")
basess("suresh","password123") 

def booking(Base):
    def wrapper(username,password,rate,status):
        while True:
            print("-----------------------THEATRE BOOKING------------------------------------")
            booked = -1 
            if username == "siva" and password == "siva123":
                print("...................login successfull..............")
                
            else:
                print("Please enter correct details")
                break 
            if  rate == 150:
                print("NON AC Theatre is allocated")
                booked = 1 
            elif rate == 200:
                print("AC Theatre is allocated")
                booked = 1 
            else:
                print('your enterd rate is not availabe')
                break 
            if booked == 1:
                status = "completed"
                Base(username,"Successful",rate,status)
                break 
    return wrapper 
@booking 
def Base(name,message,price,status):
    print(f"{name} YOUR BOOKING IS {message}")
    print(f"Rate is {price}")
    print(f"Staus:{status}") 
n = str(input("Enter the name : "))
p = str(input("Enter the password : "))
r = int(input("enter the rate : "))
Base(n,p,r,"pending")


#a decorator function in Python typically only accepts one function as a parameter
#reason why wrapper is madotary 
#1.decoraters should return wrapper 
#2.base works as wrapper and also as a base 
