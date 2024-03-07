import csv

# Supongamos que tenemos un archivo CSV llamado 'datos.csv' con las siguientes columnas: 'Nombre', 'Edad', 'Correo'

# Leer el archivo CSV existente
with open('datos.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

# Modificar los datos en la columna 'Edad'
for row in rows:
    # Supongamos que queremos incrementar la edad en 1
    row['Edad'] = str(int(row['Edad']) + 1)

# Escribir los datos actualizados en un nuevo archivo CSV
with open('datos_modificados.csv', 'w', newline='') as csvfile:
    fieldnames = ['Nombre', 'Edad', 'Correo']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Datos modificados guardados en 'datos_modificados.csv'")
