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
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
}
scrapper = cfscrape.create_scraper() # Saltarse la verificación de CloudFare Anti-bot
r = scrapper.get("https://www.liverpool.com.mx/tienda?s=mochila+dell")
listaImagen=list()
listaProducto=list ()
soup = BeautifulSoup(r.content, "html.parser")
fichaProductos = soup.find_all('section', class_="section_img_size")
counter = 0
print('entrando')
print(fichaProductos)
try:
    print('entrando')
    for element in fichaProductos:
        img_url = element.find("img", loading="lazy")['src']
        if img_url.startswith("http"):  # Verifica que img_url sea una URL válida.
            try:
                with urllib.request.urlopen(img_url) as web_file:
                    data = web_file.read()
                    file_path = f'Actividades/Practica7/Mochilas/{counter}.jpg'
                    with open(file_path, mode='wb') as imagen:
                        imagen.write(data)
                        print(f"Imagen guardada: {file_path}")
                        counter += 1
            except Exception as e:  # Captura una gama más amplia de posibles excepciones.
                print(f"Error al guardar la imagen: {e}")
except Exception as e:
    print(f"Error al procesar la imagen: {e}")