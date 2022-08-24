import requests
from time import strftime
from datetime import datetime
import operator


# Tehran coordinates:
latitude = 35.5501
longitude  = 51.5150

# Send a get request to API:
url = 'https://api.sunrise-sunset.org/json?lat='+str(latitude)+'&lng='+str(longitude)
get_response = requests.get(url)
data = get_response.json()

def convert_time(utc_time: str, time_offset: str) -> str:
    '''
    for apply time offset from UTC to Tehran timezone
    '''
    ops = { "+": operator.add, "-": operator.sub }
    UTC = str(datetime.strptime(utc_time, '%I:%M:%S %p'))[-8:]
    new_min = ops[time_offset[0]](int(UTC[3:5]),int(time_offset[3:]))
    new_hour = ops[time_offset[0]](int(UTC[:2]),int(time_offset[1:3]))
    if new_min > 60:
        new_min -= 60
        new_hour += 1
    if new_hour > 24:
        new_hour -= 24
    return  f'{new_hour}:{new_min}:{UTC[-2:]}'

# Print the results:
print('Tehran\'s Sunrise:', convert_time(data['results']['sunrise'], strftime('%z')))
print('Tehran\'s Sunset:', convert_time(data['results']['sunset'], strftime('%z')))