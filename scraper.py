import requests

url = 'http://geo.craigslist.org/iso/us/'

# user agent: what browser and what os we are using
headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/605.1'}

response = requests.get(url, headers=headers)

# print(response.status_code)
# print(response.headers)

# WEBSITE DATA: CONTENT  !!!!!!!
print(response.content)