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

def scrape_website(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract news articles
        articles = soup.find_all("article")
        extracted_data = []

        for article in articles:
            headline_tag = article.find("a", class_="JtKRv")  # News title dynamic content 
            publication_tag = article.find("div", class_="vr1PYe")  # Publication name static content 
            date_tag = article.find("time")
            headline = headline_tag.text.strip() if headline_tag and headline_tag.text.strip() else "Headline Not Available"
            publication = publication_tag.text.strip() if publication_tag else "Publication Not Available"
          
            if date_tag and date_tag.has_attr("datetime"):
                date_str = date_tag["datetime"]
                try:
                    date = parser.parse(date_str).strftime("%Y-%m-%d %H:%M:%S")  
                    
                except Exception:
                    date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")  
            else:
                date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            extracted_data.append([headline, publication, date])

        return extracted_data if extracted_data else [["No headlines found", "N/A", datetime.today().strftime("%Y-%m-%d")]]

    except Exception as e:
        return [[url, "Error fetching page", "N/A", str(e)]]

data = []
for url in urls:
    data.extend(scrape_website(url))

script_dir = os.path.dirname(os.path.abspath(__file__))   
csv_filename = os.path.join(script_dir, "scraped_headings.csv")

with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["headline", "publication", "date"])
    writer.writerows(data)

print(f"Scraping completed. Data saved to {csv_filename}") 