from lxml import etree

# Parse the XML data
xml_data = """
<?xml version="1.0" encoding="UTF-8"?>
<ies>
<nombre>IES TicArte</nombre>
<web>http://www.ticarte.com</web>
<ciclos>
<ciclo id="ASIR">
<nombre>Administración de Sistemas Informáticos en Red</nombre>
<grado>Superior</grado>
<decretoTitulo año="2009" />
</ciclo>
<ciclo id="DAW">
<nombre>Desarrollo de Aplicaciones Web</nombre>
<grado>Superior</grado>
<decretoTitulo año="2010" />
</ciclo>
<ciclo id="SMR">
<nombre>Sistemas Microinformáticos y Redes</nombre>
<grado>Medio</grado>
<decretoTitulo año="2008" />
</ciclo>
</ciclos>
</ies>
"""

# Parse the XML string into an element tree
root = etree.fromstring(xml_data.encode())

def run_xpath_query(query):
  """
  Executes an XPath query on the provided element tree and returns the results.
  """
  results = root.xpath(query)
  if results:
    # Handle different result types (text or elements)
    if isinstance(results[0], str):
      return "\n".join(results)
    else:
      return etree.tostringlist(results, encoding="utf-8")
  else:
    return "No results found for this query."

# Execute the XPath queries
queries = {
  "1. Nombre del instituto": "//ies/nombre",
  "2. Página web del instituto": "//ies/web/text()",
  "3. Nombres de ciclos formativos": "//ciclo/nombre/text()",
  "4. Siglas de ciclos formativos": "//ciclo/@id",
  "5. Años de decretos": "//ciclo/decretoTitulo/@año",
  "6. Ciclos formativos de grado medio (toda la información)": "//ciclo[@grado='Medio']",
  "7. Nombres de ciclos formativos de grado superior": "//ciclo[@grado='Superior']/nombre/text()",
  "8. Ciclos formativos anteriores a 2010 (nombres)": "//ciclo[decretoTitulo/@año < 2010]/nombre/text()",
  "9. Ciclos formativos de 2008 o 2010 (nombres)": "//ciclo[decretoTitulo/@año = 2008 or decretoTitulo/@año = 2010]/nombre/text()",
}

for name, query in queries.items():
  print(f"\n** {name} **")
  print(run_xpath_query(query))
