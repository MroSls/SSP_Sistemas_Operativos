import requests
from bs4 import BeautifulSoup
website = "https://subslikescript.com/movie/Titanic-120338"

resultado = requests.get(website)
print(resultado)#200 es que se pudo entrar

contenido = resultado.text
print(contenido)

soup = BeautifulSoup(contenido)#Acomoda las etiquetas
#print(soup)
print(soup.prettify)#Lo identa

soup1=BeautifulSoup(contenido, 'lxml')#Formato
print(soup1.prettify())

caja = soup.find('article', class_='main-article')
texto = caja.find('h1').getText()
print(texto)

caja1 = soup.find('div', class_='full-script')
transcript = caja1.get_text(strip=True, separator=' ')
print(transcript)

caja2 = soup.find(class_='plot')
texto1 = caja2.get_text(strip=True, separator=' ')
print(texto1)