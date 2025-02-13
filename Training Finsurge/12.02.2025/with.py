#with in files
with open(r"C:\Training Finsurge\11.02.2025\handle_mulitiple.py","r") as f:
    print(f.read()) 

#with in exception handling 
try:
    with open(r"C:vnwoejmvobv","r") as f:
        print(f.read()) 
except Exception as e:
    print(e)
#with in lock 
import threading 

lock = threading.Lock()

with lock:
    print("thread lock inside and its released now")

