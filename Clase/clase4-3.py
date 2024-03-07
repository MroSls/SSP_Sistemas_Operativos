import requests
from bs4 import BeautifulSoup
import csv

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537."
}

url = 'https://pokemondb.net/pokedex/all'
pag = requests.get(url, headers=headers)
soup = BeautifulSoup(pag.content, "html.parser")

Tabla = soup.find("table", class_="data-table sticky-header block-wide")
fila = Tabla.find_all("tr")
fila = Tabla.find("tbody").find_all("tr")

nombre = []

for x in fila:
    nombre.append(x.find_all("a")[0].get_text())
print(nombre)

# Open or create the csv file
with open('Clase/pokemon.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header
    writer.writerow(["Name"])

    # Write the data
    for name in nombre:
        writer.writerow([name])

'''with open('Clase/pokemon.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header
    writer.writerow(["Name"])

    # Write the data
    for name in nombre:
        writer.writerow([name])'''