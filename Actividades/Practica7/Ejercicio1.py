from bs4 import BeautifulSoup
import cfscrape
import urllib.error
import urllib.request
import csv

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
}
scrapper = cfscrape.create_scraper() # Saltarse la verificación de CloudFare Anti-bot
r = scrapper.get("https://www.lego.com/es-mx/themes/star-wars")

listaImagen=list()
listaProducto=list ()
soup = BeautifulSoup(r.content, "html.parser")

fichaProductos = soup.find_all('article', class_="ProductLeaf_wrapper__H0TCb")
    
with open("Actividades/Practica7/Legos.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write header row (optional)
    writer.writerow(["Nombre", "Precio"])

    for element in fichaProductos:
        try:
            # Extract data
            name = element.find("span", class_='markup').get_text().strip()
            price = element.find("span", class_='price-sm-bold').get_text().strip()
            img_url = element.find("img")['src']
            # Write data to CSV
            writer.writerow([name, price])
            with urllib.request.urlopen(img_url) as web_file:
                data = web_file.read()
                with open('Actividades/Practica7/Legos/'+str(name).replace(":", "_")+ ".jpg", mode='wb') as imagen:
                    imagen.write(data)
        except urllib.error.URLError as e:
            print(e)
print("Datos guardados en Legos.csv")