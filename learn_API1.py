import requests
import json
from flask import request

#Test API Stackexchange
#url = "https://api.stackexchange.com/2.3/questions?fromdate=1601510400&todate=1630368000&order=desc&sort=activity&site=stackoverflow"

#response = requests.get(url)

#for data in response.json()['items']:
#	print(data['tags'])

#Test API local
url = "http://127.0.0.1:5000/drinks"

data_json = {'name': 'Whiskey', 'description': 'Whisky or whiskey is a type of distilled alcoholic beverage made from fermented grain mash. Various grains are used for different varieties, including barley, corn, rye, and wheat.'}

response = requests.post(url, json=data_json)
print(response)
print(response.json())