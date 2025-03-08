import os
import task2
import task3
import task4
import task5
import threading

def find_csv_files(folder_path):
   
    csv_files = {"task2": None, "task3": None, "task4": None, "task5": None} 

    for file in os.listdir(folder_path):
        if file == "task2file.csv":
            csv_files["task2"] = os.path.join(folder_path, file)
        elif file == "task3file.csv":
            csv_files["task3"] = os.path.join(folder_path, file)
        elif file == "task4file.csv":
            csv_files["task4"] = os.path.join(folder_path, file) 
        elif file == "task5file.csv":
            csv_files["task5"] = os.path.join(folder_path, file) 
    return csv_files

def process_task2(csv_path):
    
    db_manager = task2.EmployeeDBManager(csv_path)
    db_manager.insert_using_executemany()
    db_manager.close_connection()

def process_task3(csv_path):
    db_manager = task3.EmployeeDBManager(csv_path)
    db_manager.insert_ignore_then_update()
    db_manager.close_connection()

def process_task4(csv_path):
    
    task4.upsert_from_csv(csv_path)

def process_task5(csv_path):
    
    db_manager = task5.EmployeeDBManager(csv_path)
    db_manager.process_data()
    db_manager.close_connection()

def main():
    folder_path = r"C:\Training Finsurge\Mini_tasks\csv_files"
    csv_files = find_csv_files(folder_path)

    threads = []

    if csv_files["task2"]:
        t2 = threading.Thread(target=process_task2, args=(csv_files["task2"],))
        threads.append(t2)
        t2.start()

    if csv_files["task3"]:
        t3 = threading.Thread(target=process_task3, args=(csv_files["task3"],))
        threads.append(t3)
        t3.start()

    if csv_files["task4"]:
        t4 = threading.Thread(target=process_task4, args=(csv_files["task4"],))
        threads.append(t4)
        t4.start()

    if csv_files["task5"]:
        t5 = threading.Thread(target=process_task5, args=(csv_files["task5"],))
        threads.append(t5)
        t5.start()
    
    # Wait 
    for thread in threads:
        thread.join()
if __name__ == "__main__":
    main()
