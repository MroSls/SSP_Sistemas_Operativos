import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the website
response = requests.get('https://pokemondb.net/pokedex/all')

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table with the data
table = soup.find('table', {'id': 'pokedex'})

# Get the table headers and rows
headers = [th.text for th in table.find('thead').find_all('th')]
rows = table.find('tbody').find_all('tr')

# Extract the data into a list of dictionaries
data = []
for row in rows:
    cols = row.find_all('td')
    data.append({
        'Name': cols[1].text,
        'HP': int(cols[4].text),
        'Attack': int(cols[5].text),
        'Defense': int(cols[6].text)
    })

# Convert the data to a pandas DataFrame and save it to a CSV file
df = pd.DataFrame(data)
df.to_csv('Actividades/Practica6/pokemon6.csv', index=False)

# Menu for sorting
while True:
    print("1. Sort by HP")
    print("2. Sort by Attack")
    print("3. Sort by Defense")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        df = df.sort_values(by='HP')
    elif choice == '2':
        df = df.sort_values(by='Attack')
    elif choice == '3':
        df = df.sort_values(by='Defense')
    elif choice == '4':
        break
    print(df)