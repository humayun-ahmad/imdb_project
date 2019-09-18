import requests
from bs4 import BeautifulSoup
import urllib.request
import random


url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"

html_doc = requests.get(url)

soup = BeautifulSoup(html_doc.text,'lxml')

td_tag = soup.find_all('img')

# img_tag = td_tag.find('img')
for one in td_tag:
	src = one['src']
	add = random.randrange(1000,10000);
	file_name = str(add)
	urllib.request.urlretrieve(src, file_name + ".jpg")
	# print(src)

# print(img)

# print(soup)
