'''Escribir una función que reciba un diccionario con las notas de los alumno de un curso y devuelva una serie con la nota mínima, la máxima, media y la desviación estandar.'''
import pandas as pd

def calcular_estadisticas(notas):
    df = pd.DataFrame.from_dict(notas, orient='index', columns=['Nota'])
    # Calcular las estadísticas
    nota_minima = df['Nota'].min()
    nota_maxima = df['Nota'].max()
    nota_media = df['Nota'].mean()
    desviacion_estandar = df['Nota'].std()
    estadisticas = pd.Series([nota_minima, nota_maxima, nota_media, desviacion_estandar], index=['Mínima', 'Máxima', 'Media', 'Desviación Estándar'])
    return estadisticas

notas = {}
while True:
    alumno = input('Ingrese "0" para terminar\nIngrese el nombre del alumno:')
    if alumno == "0":
        break
    nota = float(input('Ingrese la nota de '+alumno+': '))
    notas[alumno] = nota

print(calcular_estadisticas(notas))