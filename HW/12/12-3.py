import requests

latitude = 35.5501
longitude  = 51.5150

url = 'https://api.sunrise-sunset.org/json?lat='+str(latitude)+'&lng='+str(longitude)
method = 'GET'
get_response = requests.request(method , url)

print('\n',get_response.content)