from bs4 import BeautifulSoup
import requests

# Reemplaza la URL con la de la página que contiene la imagen
url_pagina = "https://www.walmart.com.mx/search?q=mochilas+dell"

# Descarga el contenido HTML de la página
response = requests.get(url_pagina)

# Crea un objeto BeautifulSoup a partir del contenido HTML
soup = BeautifulSoup(response.content, "html.parser")

# Encuentra la etiqueta `img` que contiene la imagen
imagen = soup.find("img", class_="absolute top-0 left-0")

# Extrae la URL de la imagen
url_imagen = imagen["srcset"]

# Descarga la imagen
response = requests.get(url_imagen)

# Guarda la imagen en un archivo
with open("/Actividades/Practica7/imagen/imagen_mochila_dell.jpg", "wb") as f:
    f.write(response.content)

print("Imagen descargada correctamente")
