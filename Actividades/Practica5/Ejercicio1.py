from bs4 import BeautifulSoup
import requests

website = 'https://es.wikipedia.org/wiki/Wikipedia:Portada'
result = requests.get(website)
content = result.text
file = 'article.txt'
goodFile = 'articleGood.txt'

soup = BeautifulSoup(content, 'html.parser')

# Extract the title of the page
title = soup.title.string

# Extract the text of the main article
article_text = soup.find('div', {'id': 'main-tfa'}).get_text()
    
# Extract the title of the main article
main_article_title = soup.find('h2', class_='main-header main-box-header').get_text()

caja = soup.find('div', class_='main-box main-box-responsive-image')
texto = caja.find('p').getText()
# Find the second 'p' tag within the div
texto2 = caja.find_all('p')[1].getText()

good_article_title = soup.find_all('h2', class_='main-header main-box-header')[1].getText()
texto3 = soup.find_all('p')[4].getText()

# Save the main article to the .txt file
with open(file, 'w', encoding='utf-8') as f:
    f.write((main_article_title + '\n' + texto + '\n' + texto2 ))

with open(goodFile, 'w', encoding='utf-8') as f:
    f.write((good_article_title + '\n' + texto3))