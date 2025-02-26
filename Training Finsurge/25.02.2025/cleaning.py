import pandas as pd
import numpy as np

# DataFrame with Null Values, Wrong Formats, and Duplicates
data = {
    "Name": ["Alice", "Bob", "Charlie", "Alice", np.nan, "David", "Eve", "Frank", "Grace", "Bob"],
    "Age": [25, "Thirty", 29, 25, 22, -5, 34, None, 40, 29],  # "Thirty" (wrong format), -5 (invalid age)
    "Salary": [50000, 60000, np.nan, 50000, 45000, 70000, 55000, 65000, None, 60000],  # Missing values
    "Join_Date": ["2021.06-15", "2021-07-20", "WrongDate", None, "2020-08-01", "2022-02-10", "2021-09-30", "Invalid", "2023-01-25", "2021-07-20"],  # Wrong formats
    "Department": ["HR", "IT", "Finance", "HR", np.nan, "IT", "Finance", "HR", "Finance", "IT"]
}

df = pd.DataFrame(data)

#Fill missing values in 'Name' and 'Department' with 'Unknown'

df["Name"] = df["Name"].fillna('Unknown') 
df["Department"] = df["Department"].fillna("Unknown") 

#filling the missing salary with meadian

df["Salary"] = df["Salary"].fillna(df["Salary"].median())

#correct the age format 
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")  # Convert to numeric
df["Age"].fillna(0, inplace=True)  
df.loc[df["Age"] < 0, "Age"] = 0  
print(df["Age"]) 

# Convert Join_Date to datetime, replacing errors with NaN

df["Join_Date"] = pd.to_datetime(df["Join_Date"],errors = "coerce") 
print(df["Join_Date"]) 

#drop duplicateds 
df = df.drop_duplicates()

# Aggregate Salary and Age by Department
df_grouped = df.groupby("Department").agg({
    "Salary": ["mean", "max", "min"],
    "Age": ["mean", "max"]
})

print("\nAggregated Data:")
print(df_grouped)

#loc -- > label based selection 
#iloc ---> index based selection 
#source : https://www.datacamp.com/tutorial/loc-vs-iloc