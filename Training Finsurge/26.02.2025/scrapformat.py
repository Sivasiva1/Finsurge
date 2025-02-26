from bs4 import BeautifulSoup

html_data = "<html><body><h1>Hello, World!</h1></body></html>"

# Using different parsers
soup1 = BeautifulSoup(html_data, "html.parser")
soup2 = BeautifulSoup(html_data, "lxml")
soup3 = BeautifulSoup(html_data, "html5lib")
soup4 = BeautifulSoup(html_data, "xml")

print("HTML Parser:", soup1.prettify())
print("LXML Parser:", soup2.prettify())
print("HTML5Lib Parser:", soup3.prettify())
print("XML Parser:", soup4.prettify())
