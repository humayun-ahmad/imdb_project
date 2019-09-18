import requests
from bs4 import BeautifulSoup

class get_movie():
	def __init__(self):
		self.rank = ""
		self.title = ""
		self.year = ""
		self.link = ""



movie_list = []

url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"

html_doc = requests.get(url)

soup = BeautifulSoup(html_doc.text,'lxml')

table_tag = soup.find('table', class_ = "chart full-width")

def get_movie_detail():

	for one_td in table_tag('td', class_ = "titleColumn"):

		result = one_td.text.strip().replace('      ','').replace('\n','')

		print(result)

		rank = result.split('.')[0]

		# print(rank)

		title = result.split('.')[1].split('(')[0]

		# print(title)

		# year = result.split('(')[1][-1]
		year = result.split('(')[1].split(')')[0]

		# print(year)

		a = one_td.find('a')
		link = "https://www.imdb.com" + a['href']

		new_movie = get_movie()

		new_movie.rank = rank
		new_movie.title = title
		new_movie.year = year
		new_movie.link = link
		movie_list.append(new_movie)

	return movie_list

		# print(link)
	# print(soup)


movie_list_all = get_movie_detail()
for one_movie in movie_list_all:
	print(one_movie.rank)
	print(one_movie.title)
	print(one_movie.year)
	print(one_movie.link)
