#single thread 
#example 1 
import threading 

def loop():
    print("--------------Thread Starts--------------")
    for i in range(5):
        print(f"Task{i}: {i*i}")

t1 = threading.Thread(target=loop)
t1.start() 
t1.join() 

#example 2 
def loop1(num1,num2):
    print("--------Thread 2 --------------------")
    
    print(num1+num2)
    print(num1-num2)
    print(num1*num2)
    print(num1//num2) 


t2 = threading.Thread(target=loop1,args=(10,10)) 

t2.start() 
t2.join() 
