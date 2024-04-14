from lxml import etree

xml = etree.parse('Clase/Actividad/ejer1.xml')

# Mostrar el nombre del instituto.
name = xml.xpath('/ies/nombre/text()')
# Mostrar la página web del instituto sin etiquetas.
web = xml.xpath('/ies/web/text()')
# Mostrar el nombre de los ciclos formativos sin etiquetas.
ciclos = xml.xpath('//ciclo/nombre/text()')
# Mostrar las siglas por las que se conocen los ciclos formativos.
siglas = xml.xpath('//ciclo/@id')
# Mostrar los años en los que se publicaron los decretos de los ciclos formativos.
años = xml.xpath('//ciclo/decretoTitulo/@año')

# Mostrar toda la información de los ciclos formativos de grado medio.
ciclos_medio = xml.xpath('//ciclo[grado="Medio"]')
print("Información de los ciclos formativos de grado medio:")
for ciclo in ciclos_medio:
    nombre = ciclo.findtext('nombre')
    sigla = ciclo.get('id')
    print(f"- {nombre} ({sigla})")

formarivos = xml.xpath("//ciclo[@grado='Medio']")
# Mostrar los nombres de los ciclos formativos de grado superior.
superior =xml.xpath("//ciclo[@grado='Superior']/nombre/text()")

# Mostrar los nombres de los ciclos formativos anteriores a 2010 sin etiquetas.
a2010 =xml.xpath('//ciclo[decretoTitulo/@año < 2010]/nombre/text()')
# Mostrar los nombres de los ciclos formativos de 2008 o de 2010.
a8a10 =xml.xpath('//ciclo[decretoTitulo/@año = 2008 or decretoTitulo/@año = 2010]/nombre/text()')
print(name)
print(web)
print(ciclos)
print(siglas)
print(años)
print(ciclos_medio)
print(formarivos)
print(superior)

print(a2010)
print(a8a10)