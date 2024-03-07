import requests
from bs4 import BeautifulSoup
import csv

url = 'https://pokemondb.net/pokedex/all'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find("table", class_="data-table sticky-header block-wide")
rows = table.find("tbody").find_all("tr")

csv_data = []
nombre = []
for x in rows:
    nombre.append(x.find_all("a")[0].get_text())
print(nombre)

for row in rows[1:]:  # skip the header row
    cols = row.find_all('td')
    csv_row = [
        cols[0].text.strip(),  # id
        #cols[1].text.strip(),  # name
        cols[4].text.strip(),  # hp
        cols[5].text.strip(),  # attack
        cols[6].text.strip(),  # defense
    ]
    csv_data.append(nombre)
    #csv_data.append(nombre)
#print(csv_data)
with open('pokemon_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ID'])
    writer.writerows(csv_data)