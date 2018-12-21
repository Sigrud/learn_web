from datetime import datetime

import requests
from bs4 import BeautifulSoup

from webapp.model import db, News

def get_html(url):
	try:
		result = requests.get(url)
		result.raise_for_status()
		return result.text
	except(requests.RequestsException, ValueError):
		return False


def get_python_news():
	html = get_html('https://www.python.org/blogs/')
	if html:
		soup = BeautifulSoup(html, 'html.parser')
		all_news = soup.find('ul', class_ = 'list-recent-posts menu').findAll('li')
		# print(all_news.findAll('a'))		
		result_news = []
		for news in all_news:
			title = news.find('a').text
			url = news.find('a')['href']
			published = news.find('time').text
			try:
				published = datetime.strptime(published, '%Y-%m-%d')
			except ValueError:
				published = datetime.now()
			save_news(title, url, published)
		
		

def save_news(title, url, published):
	news_exist = News.query.filter(News.url == url).count()
	print(news_exist)
	if not news_exist:
		news_news = News(tittle = title, url = url, published = published)
		db.session.add(news_news)
		db.session.commit()
	

# if __name__=="__main__":
# 	get_python_news()