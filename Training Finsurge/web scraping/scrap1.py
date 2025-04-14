import requests
import csv
import os
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import parser

urls = [
    "https://news.google.com/search?q=%22ford%20shares%22&hl=en-IN&gl=IN&ceid=IN%3Aen",
    "https://news.google.com/search?q=%22jio%22&hl=en-IN&gl=IN&ceid=IN%3Aen",
]

def scrape_website(url, keyword):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, "html.parser")
        
        articles = soup.find_all("article")
        extracted_data = []

        for article in articles:
            headline_tag = article.find("a", class_="JtKRv")  
            publication_tag = article.find("div", class_="vr1PYe") 
            date_tag = article.find("time")
            headline = headline_tag.text.strip() if headline_tag and headline_tag.text.strip() else "Headline Not Available"
            publication = publication_tag.text.strip() if publication_tag else "Publication Not Available"
            article_url = "https://news.google.com" + headline_tag["href"] if headline_tag and headline_tag.has_attr("href") else "URL Not Available"

            if date_tag and date_tag.has_attr("datetime"):
                date_str = date_tag["datetime"]
                try:
                    date = parser.parse(date_str).strftime("%Y-%m-%d %H:%M:%S")  
                except Exception:
                    date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")  
            else:
                date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            
            extracted_data.append([keyword,headline, publication, date, article_url])

        return extracted_data if extracted_data else [[keyword,"No headlines found", "N/A", datetime.today().strftime("%Y-%m-%d"), "N/A"]]

    except Exception as e:
        return [[ "Error fetching page", "N/A", "N/A", str(e),url]]

data = []
for url in urls:
    keyword = "Ford" if "ford" in url.lower() else "Jio" if "jio" in url.lower() else "Unknown"
    data.extend(scrape_website(url, keyword))

script_dir = os.path.dirname(os.path.abspath(__file__))   
csv_filename = os.path.join(script_dir, "new.csv")

with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file) 
    writer.writerow(["keyword","headline", "publication", "date", "url"])
    writer.writerows(data) 
    
print(f"Scraping completed. Data saved to {csv_filename}") 
