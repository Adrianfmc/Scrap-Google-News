import requests
from bs4 import BeautifulSoup

# Definición de url
url = 'https://www.nytimes.com'

# Solicitud
r1 = requests.get(url)
coverpage = r1.content

soup1 = BeautifulSoup(coverpage,'html5lib')
coverpage_news = soup1.find_all('article', class_='css-8atqhb')
len = len(coverpage_news)
text = coverpage_news[3].get_text()
link = coverpage_news[3].find('a')['href']
#print(coverpage_news[3]
print(len)
print(text)
print(url + link)

#hasta aquí llevo


#Extraer los primeros 5 artículos
number_of_articles = 5

#Limpiar las listas de contenido, links y títulos
# Empty lists for content, links and titles
news_contents = []
list_links = []
list_titles = []
