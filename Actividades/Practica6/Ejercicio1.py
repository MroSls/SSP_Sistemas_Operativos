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
with open('Actividades/Practica6/pokemon1.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header
    writer.writerow(["Name"])

    # Write the data
    for name in nombre:
        writer.writerow([name])

# Extract additional data
hp = []
attack = []
defense = []

for x in fila:
    stats = x.find_all("td", class_="cell-num")
    hp.append(int(stats[1].get_text()))
    attack.append(int(stats[2].get_text()))
    defense.append(int(stats[3].get_text()))

# Create a list of tuples with all data
pokemon_data = list(zip(nombre, hp, attack, defense))

# Function to sort data
def sort_data(data, index):
    return sorted(data, key=lambda x: x[index], reverse=True)

# Menu
while True:
    print("\n1. Show Pokemon with highest HP")
    print("2. Show Pokemon with highest Attack")
    print("3. Show Pokemon with highest Defense")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        sorted_data = sort_data(pokemon_data, 1)
        print("Pokemon with highest HP: ", sorted_data[0])
    elif choice == '2':
        sorted_data = sort_data(pokemon_data, 2)
        print("Pokemon with highest Attack: ", sorted_data[0])
    elif choice == '3':
        sorted_data = sort_data(pokemon_data, 3)
        print("Pokemon with highest Defense: ", sorted_data[0])
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")