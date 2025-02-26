import requests
from bs4 import BeautifulSoup
import csv

url = "https://github.com"  
# Send a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all("h2")   
    
    # Open a CSV file to store the data
    with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title"])  # Writing header
        
        # Write each title into the CSV file
        for i  in titles:
            writer.writerow([i.text.strip()])
    
    print("Data successfully saved to scraped_data.csv")

else:
    print("Failed to retrieve the webpage. Status Code:", response.status_code)

