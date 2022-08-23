from locale import currency
from bs4 import BeautifulSoup
import requests

url="https://www.yjc.news/fa/ratecurrency"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).content

# Parse the html content
soup = BeautifulSoup(html_content, 'html.parser')
currencies = soup.find_all("div",attrs={"class","good-name col-sm-12"})
prices = soup.find_all("div",attrs={"class","info-good col-xs-36 col-sm-12"})
indicators = []
for i in range(len(currencies)):
    dict1 = {'name': currencies[i].text, 'price': prices[i].text}
    indicators.append(dict1)

print(indicators)


