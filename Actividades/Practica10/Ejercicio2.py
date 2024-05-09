# 1. Generar un DataFrame con los datos de los cuatro ficheros.
# 2. Filtrar las columnas del DataFrame para quedarse con las
#+ columnas ESTACION, MAGNITUD, AÑO, MES y las
# correspondientes a los días D01, D02, etc.
# 3. Reestructurar el DataFrame para que los valores de los
# contaminantes de las columnas de los días aparezcan en
# una única columna.
# 4. Añadir una columna con la fecha a partir de la
# concatenación del año, el mes y el día (usar el
# módulo datetime).
# 5. Eliminar las filas con fechas no válidas (utilizar la
# función isnat del módulo numpy) y ordenar el DataFrame
# por estaciones contaminantes y fecha.
# 6. Mostrar por pantalla las estaciones y los contaminantes
# disponibles en el DataFrame.

# 7. Crear una función que reciba una estación, un contaminante
# y un rango de fechas y devuelva una serie con las emisiones
# del contaminante dado en la estación y rango de fechas
# dado.
# 8. Mostrar un resumen descriptivo (mínimo, máximo, media,
# etc.) para cada contaminante.
# 9. Mostrar un resumen descriptivo para cada contaminante por
# distritos.
# 10. Crear una función que reciba una estación y un
# contaminante y devuelva un resumen descriptivo de las
# emisiones del contaminante indicado en la estación
# indicada.c.c-231.c
# 11. Crear una función que devuelva las emisiones medias
# mensuales de un contaminante y un año dados para todos
# las estaciones.
# 12. Crear un función que reciba una estación de medición y
# devuelva un DataFrame con las medias mensuales de los
# distintos tipos de contaminantes.

import pandas as pd
import numpy as np
import datetime as dt

# Lectura de los ficheros CSV
ficheros = ["Actividades/Practica10/CSV/emisiones-2016.csv", "Actividades/Practica10/CSV/emisiones-2017.csv", "Actividades/Practica10/CSV/emisiones-2018.csv", "Actividades/Practica10/CSV/emisiones-2019.csv"]

# Lista para almacenar los DataFrames
data_frames = []

# Lectura de cada fichero CSV y almacenamiento en la lista
for fichero in ficheros:
    df_temp = pd.read_csv(fichero, sep=';')
    data_frames.append(df_temp)

# Combinación de los DataFrames en un único DataFrame
df_completo = pd.concat(data_frames, ignore_index=True)

# Selección de las columnas deseadas
columnas_seleccionadas = ["ESTACION", "MAGNITUD", "ANO", "MES"]
columnas_dias = [col for col in df_completo.columns if col.startswith("D")]
columnas_seleccionadas.extend(columnas_dias)

df_filtrado = df_completo[columnas_seleccionadas]

# Renombramiento de las columnas de los días
df_filtrado.rename(columns=lambda x: x.replace("D", ""), inplace=True)

# Creación de la columna "FECHA"
df_filtrado["FECHA"] = pd.to_datetime(df_filtrado[['ANO', 'MES', 'DIA']].astype(str))

# Eliminación de filas con fechas no válidas
df_filtrado.dropna(subset=["FECHA"], inplace=True)

# Ordenación del DataFrame por "ESTACION" y "FECHA"
df_filtrado = df_filtrado.sort_values(by=["ESTACION", "FECHA"])

# Obtención de las estaciones y contaminantes disponibles
estaciones = df_filtrado["ESTACION"].unique()
contaminantes = df_filtrado["MAGNITUD"].unique()

# Impresión de las estaciones disponibles
print("Estaciones disponibles:")
for estacion in estaciones:
    print(estacion)

# Impresión de los contaminantes disponibles
print("\nContaminantes disponibles:")
for contaminante in contaminantes:
    print(contaminante)

def emisiones_por_estacion_contaminante_fecha(estacion, contaminante, fecha_inicio, fecha_fin):
    df_filtrado = df_filtrado[(df_filtrado["ESTACION"] == estacion) & (df_filtrado["MAGNITUD"] == contaminante) & (df_filtrado["FECHA"].between(fecha_inicio, fecha_fin))]
    serie_emisiones = df_filtrado["VALOR"]
    return serie_emisiones

def resumen_descriptivo_contaminante(contaminante):
    df_filtrado = df_filtrado[df_filtrado["MAGNITUD"] == contaminante]
    resumen = df_filtrado["VALOR"].describe()
    return resumen

def resumen_descriptivo_contaminante_distrito(contaminante):
    df_agrupado_distrito = df_filtrado.groupby(["ESTACION", "MAGNITUD"])["VALOR"].mean()
    resumen_por_distrito = df_agrupado_distrito.unstack()
    return resumen_por_distrito

def emisiones_medias_mensuales_contaminante_anio(contaminante, anio):
    df_filtrado = df_filtrado[(df_filtrado["MAGNITUD"] == contaminante) & (df_filtrado["AÑO"] == anio)]
    df_agrupado_mes = df_filtrado.groupby(["MES"])["VALOR"].mean()
    return df_agrupado_mes

def resumen_medias_mensuales_estacion(estacion):
    df_filtrado = df_filtrado[df_filtrado["ESTACION"] == estacion]
    df_agrupado_mes = df_filtrado.groupby(["MAGNITUD", "MES"])["VALOR"].mean().unstack()
    return df_agrupado_mes
