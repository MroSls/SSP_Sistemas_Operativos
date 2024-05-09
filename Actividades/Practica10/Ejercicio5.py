# 1. Generar un DataFrame con los datos del fichero.
# 2. Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus
# columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas
# 3. Mostrar por pantalla los datos del pasajero con identificador 148.
# 4. Mostrar por pantalla las filas pares del DataFrame.
# 5. Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
# 6. Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
# 7. Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
# 8. Eliminar del DataFrame los pasajeros con edad desconocida.
# 9. Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
# 10. Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
# 11. Mostrar por pantalla el porcentaje de menores y
# mayores de edad que sobrevivieron en cada clase.

import pandas as pd

# 1. Generar un DataFrame con los datos del fichero.
df = pd.read_csv('Actividades/Practica10/CSV/titanic.csv')

# 2. Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas
print(df.shape)
print(df.size)
print(df.columns)
print(df.dtypes)
print(df.head(10))
print(df.tail(10))

# 3. Mostrar por pantalla los datos del pasajero con identificador 148.
print(df[df['PassengerId'] == 148])

# 4. Mostrar por pantalla las filas pares del DataFrame.
print(df.iloc[::2])

# 5. Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
print(df[df['Pclass'] == 1]['Name'].sort_values())

# 6. Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
print(df['Survived'].value_counts(normalize=True) * 100)

# 7. Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
print(df.groupby('Pclass')['Survived'].mean() * 100)

# 8. Eliminar del DataFrame los pasajeros con edad desconocida.
df = df.dropna(subset=['Age'])

# 9. Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
print(df[df['Sex'] == 'female'].groupby('Pclass')['Age'].mean())

# 10. Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
df['IsMinor'] = df['Age'] < 18

# 11. Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
print(df.groupby(['Pclass', 'IsMinor'])['Survived'].mean() * 100)
