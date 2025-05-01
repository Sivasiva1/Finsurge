import pandas as pd
import os

# Folder where the CSVs will be saved
output_folder = r"C:\Users\Nagaraja\Downloads\Training Finsurge-Siva M-Python\Training Finsurge\threadanddb\IN"  # Change this path
os.makedirs(output_folder, exist_ok=True)

# Mapping of CSV filenames and their structure
table_map = {
    "teachers.csv": "teachername",
    "students.csv": "studentname",
    "principals.csv": "principalname",
    "workers.csv": "workername",
    "clerks.csv": "clerkname",
    "employees.csv": "employeename",
    "hrs.csv": "hrname",
    "managers.csv": "managername",
    "staffs.csv": "staffname",
    "interns.csv": "internname"
}

for filename, name_col in table_map.items():
    data = {
        "id": range(1, 50001),
        name_col: [f"{name_col.capitalize()}{i}" for i in range(1, 50001)],
        "Roles": [name_col.replace("name", "").capitalize()] * 50000
    }
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(output_folder, filename), index=False)

print("All files created successfully.")
