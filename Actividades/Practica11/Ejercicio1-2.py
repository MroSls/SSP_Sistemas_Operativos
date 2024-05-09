#Para este ejercicio la variable objetivo es las ventas en taquilla de la película (la columna `venta`)
#Seleccionar las columnas numéricas sólo. Eliminar los valores nulos y reemplazarlos con 0
#Crear un modelo de regresion lineal La variable objetivo es `ventas`
#Asignar una columna nueva con las predicciones al dataset original llamada `ventas_pred`
#presupuesto,popularidad,ventas,duracion,puntuacion,n_votos
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
datos = pd.read_csv("Actividades/Practica11/movies.csv", sep=',', index_col=0)
datos = datos.replace(np.nan, 0)
variables_numericas = datos.select_dtypes(include=[np.number])
variables_numericas.drop('ventas', axis=1, inplace=True)
variables_numericas.fillna(0, inplace=True)
modelo = LinearRegression()
modelo.fit(variables_numericas, datos['ventas'])
datos['ventas_pred'] = modelo.predict(variables_numericas)
datos = datos.select_dtypes(include=np.number)
datos.to_csv('Actividades/Practica11/new_movies.csv')