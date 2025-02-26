import pandas as pd 

data = pd.read_csv(r"C:\Training Finsurge\26.02.2025\messy_data.csv") 

data["Salary"] = data["Salary"].astype(float)  # Convert to float
data["Name"].fillna("Unkown",inplace = True) 

print(data.duplicated().sum())  # Count duplicate rows

data["Age"].fillna(data["Age"].median(),inplace = True) 


data["Age"] = data["Age"].astype(int) #to int 
data["Salary"].fillna(data["Salary"].median(),inplace = True) 


data["Department"].fillna(data["Department"].mode()[0] , inplace=True) 

data["Email"] = data["Email"].str.replace("_at_", "@") 

def clean_date(date):
        try:
            return pd.to_datetime(date,errors = "coerce").strftime("%Y-%m-%d")
        except:
              return None 
data["Joining Date"] = data["Joining Date"].apply(clean_date) 

print(data) 



df_high_salary = data[data["Salary"] > 50000]  
df_IT = data[data["Department"] == "IT"]  
print("------------high salary---------------")
print(df_high_salary)

print("---------------IT DEPARTMENT--------------")
print(df_IT) 