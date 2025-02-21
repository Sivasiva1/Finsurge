import threading 

lock = threading.Lock()

count = 0 

def counting():
    global count 
    with lock:
        for i in range(10000):
            count+=1 

t1 = threading.Thread(target=counting) 
#again locked when t1 is finished 
t2 = threading.Thread(target=counting)
t1.start()
t2.start()

t1.join()
t2.join()

print(count) 

import threading

lock = threading.Lock()
list1 = []  

def append_numbers():
    for i in range(5):
        with lock:  # Ensuring only one thread modifies the list at a time
            list1.append(i)
            print(f"{threading.current_thread().name} added {i}")

t3 = threading.Thread(target=append_numbers, name="Thread-1")
t4 = threading.Thread(target=append_numbers, name="Thread-2")

t3.start()
t4.start()

t3.join()
t4.join()

print("Final List:", list1)
