import pandas as pd 

series_list = pd.Series([10, 20, 30, 40, 50,50])
series_dict = pd.Series({'a': 100, 'b': 200, 'c': 300})

print(series_list)
print(series_dict)
 

print("FIRST ONE ROWS :" ,series_dict.head(1))
print("LAST TWO ROWS :" , series_list.tail(2)) 

#max, min, mean, std 

print("maximum :" ,series_list.max(),"minimum:" ,series_list.min(),"mean " ,series_list.mean()) 

#value counts 
print("-----unique value counts ---------")
print(series_list.value_counts()) 

#upper case and lower case 
string_series = pd.Series(["hello", "world", "pandas"])
print(string_series.str.upper())
print(string_series.str.lower()) 

