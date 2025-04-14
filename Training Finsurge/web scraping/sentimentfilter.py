import pandas as pd 
df_new = pd.read_csv(r"C:\Users\Nagaraja\Downloads\Training Finsurge-Siva M-Python\titlewithsentiment.csv")

print("-------------------------------Each number of sentiments-----------------------------")
print("Total number of positives:" , (df_new["sentiment"]=="positive").sum()) 
print("Total number of negatives:",(df_new["sentiment"]=="negative").sum()) 
print("total number of neutrals:",(df_new["sentiment"]=="neutral").sum()) 

print("------------------------date base sentiment count-----------------------------")
sentiment_by_date = df_new.groupby(['date', 'sentiment']).size().unstack().fillna(0)
print(sentiment_by_date)

print("----------------------------top publisher with positive-------------------------")
top_publisher = df_new[df_new["sentiment"]=="positive"]["publication"].head(3) 
print(top_publisher) 

print("---------------- Filter headlines containing a keyword + sentiment ------------------------")
key_row = df_new[(df_new["sentiment"]=="negative") & (df_new["headline"].str.contains("losses",case=False,na=False))] 
print(key_row) 

key_row = df_new[(df_new["sentiment"]=="positive") & (df_new["headline"].str.contains("trading",case=False,na=False))] 
print(key_row) 

print("------------------Top publishers by each sentiment ---------------------") 
top_publishers_sentiment = df_new.groupby(['publication', 'sentiment']).size().unstack().fillna(0)
print(top_publishers_sentiment.sort_values(by='positive', ascending=False).head(5)) 



