# 1. Diagrama de sectores con los fallecidos y supervivientes.
# 2. Histograma con las edades.
# 3. Diagrama de barras con el número de personas en cada clase.
# 4. Diagrama de barras con el número de personas fallecidas y
# supervivientes en cada clase.
# 5. Diagrama de barras con el número de personas fallecidas y
# supervivientes acumuladas en cada clase.
import pandas as pd
import matplotlib.pyplot as plt
file = 'Actividades/Practica10/CSV/titanic.csv'
# Definir los datos
datos = {
    "Nombre": ["Ana", "Juan", "Maria", "Pedro", "Rosa", "Luis", "Carlos"],
    "Edad": [25, 30, 22, 45, 33, 28, 50],
    "Clase": ["A", "B", "A", "B", "C", "B", "A"],
    "Fallecido": [False, True, False, False, True, False, False],
}

# Crear el DataFrame
df = pd.read_csv(file)

# 1. Diagrama de sectores con los fallecidos y supervivientes
fallecidos = df[df["Survived"] == False].shape[0]
supervivientes = df[df["Survived"] == True].shape[0]
plt.figure(figsize=(6, 6))
plt.pie([fallecidos, supervivientes], labels=["Fallecidos", "Supervivientes"], autopct="%1.1f%%")
plt.title("Fallecidos vs Supervivientes")
plt.show()

# 2. Histograma con las edades
plt.figure(figsize=(8, 6))
plt.hist(df["Age"], bins=10, edgecolor="black")
plt.xlabel("Edad")
plt.ylabel("Número de personas")
plt.title("Distribución de edades")
plt.grid(True)
plt.show()

# 3. Diagrama de barras con el número de personas en cada clase
clases_agrupadas = df["Pclass"].value_counts()
plt.figure(figsize=(8, 6))
clases_agrupadas.plot(kind="bar", color=plt.cm.viridis.colors)
plt.xlabel("Clase")
plt.ylabel("Número de personas")
plt.title("Número de personas en cada clase")
plt.grid(True)
plt.show()

# 4. Diagrama de barras con el número de personas fallecidas y
# supervivientes en cada clase
fallecidos_por_clase = df.groupby("Pclass")["Survived"].sum()
supervivientes_por_clase = df[df["Survived"] == False].groupby("Pclass").size()
plt.figure(figsize=(12, 6))
fallecidos_por_clase.plot(kind="bar", label="Fallecidos", color="red")
supervivientes_por_clase.plot(kind="bar", label="Supervivientes", color="green")
plt.xlabel("Clase")
plt.ylabel("Número de personas")
plt.title("Número de personas fallecidas y supervivientes en cada clase")
plt.grid(True)
plt.legend()
plt.show()

# 5. Diagrama de barras con el número de personas fallecidas y
# supervivientes acumuladas en cada clase
fallecidos_acumulados = fallecidos_por_clase.cumsum()
supervivientes_acumulados = supervivientes_por_clase.cumsum()
plt.figure(figsize=(12, 6))
fallecidos_acumulados.plot(kind="bar", label="Fallecidos acumulados", color="red")
supervivientes_acumulados.plot(kind="bar", label="Supervivientes acumulados", color="green")
plt.xlabel("Clase")
plt.ylabel("Número de personas")
plt.title("Número de personas fallecidas y supervivientes acumuladas en cada clase")
plt.grid(True)
plt.legend()
plt.show()
