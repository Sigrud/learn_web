import requests
from bs4 import BeautifulSoup

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
			tittle = news.find('a').text
			url = news.find('a')['href']
			published = news.find('time').text
			result_news.append({
				'tittle' : tittle,
				'url' : url,
				'publish' : published
				})
		# print (result_news)

		return result_news		
	return False
	

# if __name__=="__main__":
# 	get_python_news()