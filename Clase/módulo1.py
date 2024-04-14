import requests
from bs4 import BeautifulSoup
import html5lib

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537."
}
url = 'https://es.99designs.com/inspiration/logos/distressed'
html = requests.get(url, headers=headers)
soup = BeautifulSoup(html.text, 'html5lib')

imagelink = soup.find("img",class_="design-figure__image-container__image").get('src')


print(imagelink)