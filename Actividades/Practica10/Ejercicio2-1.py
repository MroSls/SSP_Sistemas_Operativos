import pandas as pd
import numpy as np
from datetime import datetime

# 1. Generar un DataFrame con los datos de los cuatro ficheros.
df = pd.concat([pd.read_csv(f'Actividades/Practica10/CSV/emisiones-{year}.csv', sep=';') for year in range(2016, 2020)])
df = pd.read_csv(file, sep=';', decimal=',', thousands='.', index_col=0)
# 2. Filtrar las columnas del DataFrame
columns = ['ESTACION', 'MAGNITUD', 'ANO', 'MES'] + [f'D{i:02}' for i in range(1, 31)]
df = df[columns]

# 3. Reestructurar el DataFrame
df = df.melt(id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='DIA', value_name='VALOR')
df['DIA'] = df['DIA'].str[1:].astype(int)

# 4. Añadir una columna con la fecha
df['FECHA'] = df.apply(lambda row: datetime(row['ANO'], row['MES'], row['DIA']), axis=1)

# 5. Eliminar las filas con fechas no válidas y ordenar el DataFrame
df = df.drop(df[np.isnat(df['FECHA'])].index)
df = df.sort_values(['ESTACION', 'MAGNITUD', 'FECHA'])

# 6. Mostrar por pantalla las estaciones y los contaminantes disponibles en el DataFrame
print(df['ESTACION'].unique())
print(df['MAGNITUD'].unique())

# 7. Crear una función que reciba una estación, un contaminante y un rango de fechas
def get_emissions(station, pollutant, start_date, end_date):
    mask = (df['ESTACION'] == station) & (df['MAGNITUD'] == pollutant) & (df['FECHA'] >= start_date) & (df['FECHA'] <= end_date)
    return df.loc[mask, 'VALOR']

# 8. Mostrar un resumen descriptivo para cada contaminante
print(df.groupby('MAGNITUD')['VALOR'].describe())

# 9. Mostrar un resumen descriptivo para cada contaminante por distritos
# Aquí asumimos que tienes una columna 'DISTRITO' en tu DataFrame
print(df.groupby(['DISTRITO', 'MAGNITUD'])['VALOR'].describe())

# 10. Crear una función que reciba una estación y un contaminante
def get_summary(station, pollutant):
    mask = (df['ESTACION'] == station) & (df['MAGNITUD'] == pollutant)
    return df.loc[mask, 'VALOR'].describe()

# 11. Crear una función que devuelva las emisiones medias mensuales de un contaminante y un año dados
def get_monthly_avg(pollutant, year):
    mask = (df['MAGNITUD'] == pollutant) & (df['AÑO'] == year)
    return df.loc[mask].groupby(['ESTACION', 'MES'])['VALOR'].mean()

# 12. Crear un función que reciba una estación de medición
def get_monthly_avg_by_pollutant(station):
    mask = df['ESTACION'] == station
    return df.loc[mask].groupby(['MAGNITUD', 'MES'])['VALOR'].mean()
