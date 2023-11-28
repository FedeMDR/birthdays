import json
import requests


test = "http://api.openweathermap.org/data/2.5/air_pollution?lat=40.68457&lon=-73.91181&appid=596dff3ac05aeb906e63803d2bfcf01a"

response = requests.get(test)

json_data = response.json()

print(json_data)