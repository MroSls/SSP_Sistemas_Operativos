'''El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Escribir un programa con los siguientes requisitos:Generar un DataFrame con los datos del fichero.
Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas,
las 10 primeras filas y las 10 últimas filasMostrar por pantalla los datos del pasajero con identificador 148.Mostrar por pantalla las filas pares del DataFrame.
Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
Eliminar del DataFrame los pasajeros con edad desconocida.Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.'''
import pandas as pd

# Generar un DataFrame con los datos del fichero
df = pd.read_csv('Actividades/Practica2/titanic.csv')

# Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas
print(df.shape)
print(df.size)
print(df.columns)
print(df.index)
print(df.dtypes)
print(df.head(10))
print(df.tail(10))

# Mostrar por pantalla los datos del pasajero con identificador 148
print(df.loc[147])

# Mostrar por pantalla las filas pares del DataFrame
print(df.iloc[::2])

# Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente
primera_clase = df[df['Pclass'] == 1]
print(primera_clase['Name'].sort_values())

# Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron
print(df['Survived'].value_counts(normalize=True) * 100)

# Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase
print(df.groupby('Pclass')['Survived'].mean() * 100)

# Eliminar del DataFrame los pasajeros con edad desconocida
df = df[df['Age'].notna()]

# Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase
print(df[df['Sex'] == 'female'].groupby('Pclass')['Age'].mean())

# Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no
df['Menor_de_edad'] = df['Age'] < 18

# Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase
print(df.groupby(['Pclass', 'Menor_de_edad'])['Survived'].mean() * 100)
