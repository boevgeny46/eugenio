import json
#
# pets = {'name': 'Charly', 'age': 15, 'meals': ['Purina', 'hills']}
#
#
# with open('pets.json') as pet_file:
#     string = pet_file.read()
#     data = json.loads(string)
#
# for item in data:
#     if type( data[item]) == list:
#         print(item, ','. join(data[item]))
#     elif type( data[item]) == dict:
#         print(item)
#

#print(data)

import json
import requests     # библиотека для http апросов


key = '1790ad380e43846114e7751a33461c2a'
url = 'http://api.openweathermap.org/data/2.5/weather'
params = {'APPID': key, 'q': 'Москва', 'units': 'metric'}

request = requests.get(url, params=params)

result = request.json()
print(result)

data = result['main']
print(f'temperature: {data["temp"]: .1f}\xB0C')
print(result['sys'])
print (f'координаты: {result["coord"] ["lon"]}, {result["coord"] ["lat"]}')  # программа работает
