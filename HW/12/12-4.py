from bs4 import BeautifulSoup
import requests
from unidecode import unidecode
from datetime import datetime
import json

url="https://www.time.ir/"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).content

# Parse the html content
soup = BeautifulSoup(html_content, 'html.parser')
times = soup.find_all("div",attrs={"class","col-sm-6"})

time_dict = {
    "azane_sobh": unidecode(times[6].text[10:17]),
    "tolooe_khorshid": unidecode(times[6].text[31:38]),
    "azane_zohr": unidecode(times[6].text[49:56]),
    "ghoroobe_khorshid": unidecode(times[7].text[13:20]),
    "azane_maghreb": unidecode(times[7].text[32:39]),
    "nime_shab": unidecode(times[7].text[54:61])   
}

for i in time_dict:
    time_dict[i] = datetime.strptime(time_dict[i], '%H : %M').strftime("%I:%M %p")

with open('times.json', 'w', encoding ='utf8') as json_file:
            json.dump(time_dict, json_file, indent = 4)



