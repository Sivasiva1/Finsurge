import pandas as pd 
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
data = pd.read_csv(r"C:\Users\Nagaraja\Downloads\Training Finsurge-Siva M-Python\Training Finsurge\web scraping\scraped_headings.csv")

analyzer = SentimentIntensityAnalyzer()
def sentimentscore(text):
    score = analyzer.polarity_scores(str(text)) 
    if score["compound"]>=0.05:
        return "positive"
    elif score["compound"]<=-0.05:
        return "negative"
    else: 
        return "neutral"

data["sentiment"] = data["headline"].apply(sentimentscore) 

data.to_csv("titlewithsentiment.csv",index=False) 
