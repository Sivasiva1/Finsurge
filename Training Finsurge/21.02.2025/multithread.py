
#asynchronized or multithreading 
#more threads - 1 task 
import threading 
import time 
def loop(string):

    for i in range(1,11):
        print(f"Task Name {string} : {i}")
        time.sleep(1)
t1 = threading.Thread(target=loop,args=("T1",))
t2 = threading.Thread(target=loop,args=("T2",))
t1.start() 
t2.start()

t1.join() 
t2.join() 
#t2 want some time to join in task so that sleep is used 
#1 thread - multiple task 

def calc():
        print("----------------T3 TASK------------------------")
        def task1():
             for i in range(1,3):
                print("task1 is executed")
                time.sleep(1)
        def task2():
            for i in range(1,3):
                print("tas2 is completed ")
                time.sleep(1) 
   
        def task3():
             for i in range(1,3):
                print("task3 is completed ")
                time.sleep(1) 
        task1()
        task2()
        task3()

t3 = threading.Thread(target=calc) 
t3.start()
t3.join()

#3.mulitiple thread and multiple task 
def task1():
    for i in range(3):
        print("Task 1 is running")
        time.sleep(1)

def task2():
    for i in range(3):
        print("Task 2 is running")
        time.sleep(1)

t4 = threading.Thread(target=task1)
t5 = threading.Thread(target=task2)

t4.start()
t5.start()

t4.join()
t5.join()

print("Both tasks completed.")
