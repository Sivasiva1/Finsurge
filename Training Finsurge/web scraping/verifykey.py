import requests
from bs4 import BeautifulSoup
urls = [
    "https://news.google.com/search?q=%22ford%20shares%22&hl=en-IN&gl=IN&ceid=IN%3Aen",
    "https://news.google.com/search?q=%22jio%22&hl=en-IN&gl=IN&ceid=IN%3Aen",
]

def check_keyword_in_page(url, keyword):
    try:
        res = requests.get(url,timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        return keyword.lower() in soup.get_text().lower()
    except Exception as e: 
        print(f"Error loading article: {url} -> {e}")
        return False

def scrape_and_verify(url, keyword):
    available_in_heading = 0 
    available_in_page = 0 
    not_available = 0 
    total = 0 
    no_url=[]
    try: 
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        articles = soup.find_all("article")
        print(f"\n Checking articles for keyword: '{keyword}'")

        for article in articles:
            headline_tag = article.find("a", class_="JtKRv") 
            headline = headline_tag.text.strip() if headline_tag else "No Headline"
            article_url = "https://news.google.com" + headline_tag["href"][1:] if headline_tag and headline_tag.has_attr("href") else None

            if keyword.lower() in headline.lower(): 
                available_in_heading+=1
                total+=1 
            elif article_url:
                found_in_page = check_keyword_in_page(article_url, keyword) 
                if found_in_page:
                     available_in_page+=1  
                else:
                    not_available+=1 
                    no_url.append(article_url) 
                total+=1 
            else:
                not_available+=1 
                no_url.append(article_url) 
                total+=1 
        for i in no_url: 
            print(i) 
        return [f"total : {total}, keywords in heading:{available_in_heading}, keyword in page:{available_in_page},keyword not present: {not_available}"]
    except Exception as e:
        print(f"Error scraping {url}: {e}") 

for url in urls:
    keyword = "Ford" if "ford" in url.lower() else "Jio" if "jio" in url.lower() else "Unknown"
    data = scrape_and_verify(url, keyword) 
    print(data) 

