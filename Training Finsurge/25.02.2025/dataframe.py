import pandas as pd 
import numpy as np 
d = {"Name ": ['Siva','Nagaraja','Manikandan','Bala','Bala'],
             "Age " :[20,30,40,50,50],
             "Salary " :[10000,2000,300,5000,5000]} 

df = pd.DataFrame(d) 
print("------------------------Dataframe--------------------------")
print(df) 

print("----------------total rows and cols----------------")
print(df.shape)  

#Rename column names

print("-------------renamed dataframe -----------------------")
df1 = df.rename(columns={"Name " : "Emp name "})
print(df1) 


#remove duplicates 
print("-----------------------------after removing duplicates------------------------------------")

new_df = df1.drop_duplicates()  
print(new_df)   

print("----------------------------index based search-------------------------------------------")
print(new_df.iloc[0:2 , 0:2])  # Using iloc (index-based)

print("-------------------Conatins-----------------------------------------")
print(new_df[new_df["Emp name "].str.contains("s" , case = False)]) 

print("-----------------------sorting in ascending order ------------------------------------------")
print(new_df.sort_values(by="Age ")) 

print("--------------------Descinding order------------------------")
print(new_df.sort_values(by="Age ",ascending = False) ) 

print("-----------------------Group by ---------------------------")
# Group by categorical column and compute aggregate functions
print(new_df.groupby('Emp name ').agg({'Age ': ['mean', 'sum']})) 

#pivot table 
print(new_df.pivot_table(values='Salary ', index='Age ', aggfunc='mean')) 

print("-------------------new column(square age)------------------------")
new_df["square age"] = new_df["Age "].apply(lambda x : x * 2) 
print(new_df) 

print("---------------------new column(category)----------------------")
new_df["category"] = np.where(new_df["Age "] > 20 , 'senior' , 'junior') 
print(new_df) 

#merge()
df2 = pd.DataFrame({'Emp name ': ['Siva', 'Bala'], 'Department': ['HR', 'IT']}) 
print("---------inner join-------------")
print(new_df.merge(df2 , on = "Emp name " , how = "inner")) 

print("----------------left join ---------")
print(new_df.merge(df2 , on = "Emp name " , how = "left")) 

print("-------------rigth join --------------")
print(new_df.merge(df2 , on = "Emp name " , how = "right")) 
