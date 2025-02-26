import pandas as pd
data = {
    'Event': ['A', 'B', 'C', 'D'],
    'Date': ['2024-02-10', '2024-03-15', '2024-04-20', '2024-05-25']
}

df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(df["Date"]) 
df["year"] = df["Date"].dt.year 
df["month"] = df['Date'].dt.month 
df["day"] = df["Date"].dt.day 

print(df) 