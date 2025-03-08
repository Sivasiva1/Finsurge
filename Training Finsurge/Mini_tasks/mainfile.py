import os
import task2
import task3
import task4 
import task5 
def find_csv_files(folder_path):
    csv_files = {"task2": None, "task3": None, "task4": None,"task5":None} 

    for file in os.listdir(folder_path):
        if file == "task2file.csv":
            csv_files["task2"] = os.path.join(folder_path, file)
        elif file == "task3file.csv":
            csv_files["task3"] = os.path.join(folder_path, file)
        elif file == "task4file.csv":
            csv_files["task4"] = os.path.join(folder_path, file) 
        elif file == "task5file.csv":
            csv_files["task5"] = os.path.join(folder_path,file) 
    return csv_files

def main():
    folder_path = r"C:\Training Finsurge\Mini_tasks\csv_files"
    csv_files = find_csv_files(folder_path)

    if csv_files["task2"]:
        db_manager = task2.EmployeeDBManager(csv_files["task2"])
        db_manager.insert_using_executemany()
        db_manager.close_connection()
    
    if csv_files["task3"]:
        db_manager = task3.EmployeeDBManager(csv_files["task3"])
        db_manager.insert_ignore_then_update()
        db_manager.close_connection()
    if csv_files["task4"]:
            task4.upsert_from_csv(csv_files["task4"])  
    if csv_files["task5"]:
            db_manager = task5.EmployeeDBManager(csv_files["task5"])
            db_manager.process_data()
            db_manager.close_connection()

if __name__ == "__main__":
    main()
