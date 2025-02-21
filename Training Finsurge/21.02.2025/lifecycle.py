import threading
import time

def thread_function():
    print("Thread is running (RUNNING STATE)...")
    time.sleep(2)  # create some time for other thread 
    print("Thread execution finished (TERMINATED STATE)")

# NEW STATE: 
thread = threading.Thread(target=thread_function)
print("Thread created but not started (NEW STATE)...")

# RUNNABLE STATE: 
thread.start()
print("Thread is ready to run (RUNNABLE STATE)...")

# WAITING STATE: 
thread.join()
