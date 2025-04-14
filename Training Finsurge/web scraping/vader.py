from nltk.sentiment.vader import SentimentIntensityAnalyzer 

analyzer = SentimentIntensityAnalyzer()
def sentimentscore(text):
    score = analyzer.polarity_scores(text) 
    print(score) 
        
    if score["compound"]>=0.05:
        print("positive")
    elif score["compound"]<=-0.05:
        print("negative") 
    else:
        print("neutral") 
text = "I love this product , the delivery was terrible."
text1 = "I love this product but the delivery was terrible"
sentimentscore(text)
sentimentscore(text1) 