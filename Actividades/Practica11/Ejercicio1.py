#Para este ejercicio la variable objetivo es las ventas en taquilla de la película (la columna `venta`)
#Seleccionar las columnas numéricas sólo. Eliminar los valores nulos y reemplazarlos con 0
#Crear un modelo de regresion lineal La variable objetivo es `ventas`
#Asignar una columna nueva con las predicciones al dataset original llamada `ventas_pred`
#presupuesto,popularidad,ventas,duracion,puntuacion,n_votos
import pandas as pd
import numpy as np

file = 'Actividades/Practica11/movies.csv'
df = pd.read_csv(file, sep=',', index_col=0)
print(df.head())
df = df.replace(np.nan, 0)
titulo = df['titulo']
ambos = df.select_dtypes(include=np.number)
print(ambos)
df =ambos
df.to_csv('Actividades/Practica11/new_movies1.csv')
print(df.head())