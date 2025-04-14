from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Set up headless Chrome
options = Options()
options.headless = True
service = Service() 
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.google.com/search?q=google+stock+nvidia+news&tbm=nws"
driver.get(url)
time.sleep(3)

soup = BeautifulSoup(driver.page_source, 'html.parser')
articles = soup.find_all('div', class_='SoaBEf')

for article in articles:
    # Headline
    title_tag = article.find('div', class_='n0jPhd ynAwRc MBeuO nDgy9d')
    headline = title_tag.text.strip() if title_tag else "N/A"

    # Publisher is the <span> tag immediately after <g-img> (logo image)
    publisher_tag = article.select_one('g-img + span')
    publisher = publisher_tag.text.strip() if publisher_tag else "N/A"

    # Date is inside a div with class like 'OSrXXb rbYSKb LfVVr'
    date_div = article.find('div', class_='OSrXXb rbYSKb LfVVr')
    date = date_div.text.strip() if date_div else "N/A"

    print(f"Headline: {headline}")
    print(f"Publisher: {publisher}")
    print(f"Date: {date}")
    print("-" * 50)
driver.quit()
