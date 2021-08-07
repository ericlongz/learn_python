import requests
import json

url = "https://api.stackexchange.com/2.3/questions?fromdate=1601510400&todate=1630368000&order=desc&sort=activity&site=stackoverflow"

response = requests.get(url)

for data in response.json()['items']:
	print(data['tags'])