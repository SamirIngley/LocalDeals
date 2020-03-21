import requests
from bs4 import BeautifulSoup as bs


url = 'https://www.macys.com/'
headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/605.1'}
response = requests.get(url, headers=headers)

print(response.status_code)

soup = bs(response.content, 'html.parser')
# print(soup.prettify)

sales = soup.find_all('ul')
print(sales)


# url = 'http://geo.craigslist.org/iso/us/'

# # user agent: what browser and what os we are using
# headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/605.1'}

# response = requests.get(url, headers=headers)

# # Make sure it works
# # print(response.status_code)

# # print(response.headers)

# # WEBSITE DATA: CONTENT  !!!!!!!
# # print(response.content)

# soup = bs(response.content, 'html.parser')
# # print(soup.prettify)

# ul_lists = soup.find_all('ul')
# # print(ul_lists)

# city_list = soup.find('ul', {'class': 'height6'})
# print(city_list)

# city_dict = {}
# for city in city_list.find_all('a'): # all <a> tags
#     city_dict[city.text] = city['href']

# for k,v in city_dict.items():
#     print(k,v)