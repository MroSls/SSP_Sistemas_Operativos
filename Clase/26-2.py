from bs4 import BeautifulSoup
import requests

website = 'https://es.wikipedia.org/wiki/Wikipedia:Portada'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())

box = soup.find('article', class_='main-article')
title = box.find('h1').get_text()
transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

with open(f'{title}.txt', 'w') as file:
    file.write(transcript)

'''from bs4 import BeautifulSoup
import requests

website = 'https://es.wikipedia.org/wiki/Wikipedia:Portada'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())

title = soup.find('h1', class_='firstHeading').get_text()

with open(f'{title}.txt', 'w') as file:
    file.write(title)'''
