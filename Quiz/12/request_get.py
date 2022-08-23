import requests


url = 'https://ipinfo.io/json'
get_response = requests.get(url)
data = get_response.json()

print('my_city is', data['city'])
print('my_region is', data['region'])
print('my_country is', data['country'])