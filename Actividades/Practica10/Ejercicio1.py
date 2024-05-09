# Construir una función que construya un DataFrame a partir del un
# fichero con el formato anterior y devuelva otro DataFrame con el
# mínimo, el máximo y la media de dada columna.

file = 'Actividades/Practica10/CSV/cotizacion.csv'
mmm = 'Actividades/Practica10/CSV/min_max_media.csv'

import pandas as pd

def process_file(file_name):
    # Leer el fichero csv
    df = pd.read_csv(file_name, sep=';', index_col=0)

    # Crear un nuevo DataFrame con el mínimo, el máximo y la media de cada columna
    df = df.replace(',', '0')
    result = pd.DataFrame({
        'Minimo': df.min(),
        'Maximo': df.max(),
    })

    return result

# Uso de la función
result = process_file(file)
print(result)
