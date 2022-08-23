import requests
from datetime import datetime

latitude = 35.5501
longitude  = 51.5150

url = 'https://api.sunrise-sunset.org/json?lat='+str(latitude)+'&lng='+str(longitude)
get_response = requests.get(url)
data = get_response.json()
print(data['results'])

# from datetime import datetime
# m2 = 'Dec 14 2018 1:07AM'
# m2 = datetime.strptime(m2, '%b %d %Y %I:%M%p')
# print(m2)


# UTC_datetime = datetime.utcnow()
# print(UTC_datetime)
# UTC_datetime_timestamp = float(UTC_datetime.strftime("%s"))
# print(UTC_datetime_timestamp)
# local_datetime_converted = datetime.fromtimestamp(UTC_datetime_timestamp)