import requests
from bs4 import BeautifulSoup
url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"

response = requests.get(url)

soup = BeautifulSoup(response.text,'lxml')

movie_title = soup.find_all('td', class_ = "titleColumn")

for one_title in movie_title:
	a_tag = one_title.find('a')
	print(a_tag.text)

# print(title)
# print(soup)