import threading

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content) 
    except Exception as e:
        print(f"Error reading {filename}: {e}")

# List of files to read
files = [r"C:\Training Finsurge\21.02.2025\text1", r"C:\Training Finsurge\21.02.2025\text2"]

threads = []
for i in files:
      t = threading.Thread(target=read_file,args=(i,))
      threads.append(t)
      t.start()
print(threads) 
for i in threads:
    i.join() 


