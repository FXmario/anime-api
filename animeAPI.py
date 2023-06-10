import json
import requests

url = "https://api.jikan.moe/v4/anime/47917/full"
response = requests.get(url)
result_all = json.dumps(response.json(), indent = 3)
result = response.json()
print(result_all)
#print(result['data']['title'])


