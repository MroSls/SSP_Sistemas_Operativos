import requests
from bs4 import BeautifulSoup
import pandas as pd
import cfscrape
import os
import pprint
import time
import urllib.error
import urllib.request

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537."
}
scrapper = cfscrape.create_scraper() # Saltarse la verificación de CloudFare Anti-bot
r = scrapper.get("https://hidralistico.com.mx/categoria-producto/juegos-de-cartas/yu-gi-oh/carta-suelta/zombie-horde/")

listaImagen=list()
listaProducto=list ()
soup = BeautifulSoup(r.content, "html.parser")
fichaProductos = soup.find_all('div', class_="box-image")
counter = 0
print(fichaProductos)
for element in fichaProductos:
    img_url = element.find("img")['data-lazy-src']
    try:
        with urllib.request.urlopen(img_url) as web_file:
            data = web_file.read()
            with open('Clase/imagen/'+str(counter) + ".jpg", mode='wb') as imagen:
                imagen.write(data)
                counter = counter + 1
    except urllib.error.URLError as e:
        print(e)