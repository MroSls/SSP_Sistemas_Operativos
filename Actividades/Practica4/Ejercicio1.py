import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
titanic_df = pd.read_csv('Actividades/Practica4/titanic.csv')
titanic_df['Sex'] = titanic_df['Sex'].astype('category')
titanic_df['Age'] = pd.to_numeric(titanic_df['Age'], errors='coerce')
titanic_df['Age'].fillna(titanic_df['Age'].median(), inplace=True)
total_passengers = titanic_df.shape[0]
print(f"Número total de pasajeros: {total_passengers}")
fallecidos = titanic_df[titanic_df['Survived'] == 0].shape[0]
supervivientes = titanic_df[titanic_df['Survived'] == 1].shape[0]
print(f"Fallecidos: {fallecidos}")
print(f"Supervivientes: {supervivientes}")
plt.figure(figsize=(10, 10))
plt.pie([fallecidos, supervivientes], labels=['Fallecidos', 'Supervivientes'], autopct='%1.1f%%')
plt.title('Proporción de fallecidos y supervivientes')
plt.show()
plt.figure(figsize=(10, 10))
sns.histplot(data=titanic_df, x='Age', color='blue')
plt.title('Distribución de edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()
sns.countplot(x='Pclass', data=titanic_df)
plt.title('Número de personas por clase')
plt.xlabel('Clase')
plt.ylabel('Número de personas')
plt.show()
fallecidos_por_clase = titanic_df[titanic_df['Survived'] == 0].groupby('Pclass').size()
supervivientes_por_clase = titanic_df[titanic_df['Survived'] == 1].groupby('Pclass').size()

df_fallecidos_supervivientes = pd.DataFrame({'Fallecidos': fallecidos_por_clase, 'Supervivientes': supervivientes_por_clase})

plt.figure(figsize=(10, 10))
df_fallecidos_supervivientes.plot.bar()
plt.title('Número de personas fallecidas y supervivientes por clase')
plt.xlabel('Clase')
plt.ylabel('Número de personas')
plt.show()
fallecidos_por_clase_acum = fallecidos_por_clase.cumsum()
supervivientes_por_clase_acum = supervivientes_por_clase.cumsum()

df_fallecidos_supervivientes_acum = pd.DataFrame({'Fallecidos': fallecidos_por_clase_acum, 'Supervivientes': supervivientes_por_clase_acum})

plt.figure(figsize=(10, 10))
df_fallecidos_supervivientes_acum.plot.bar()
plt.title('Número de personas fallecidas y supervivientes acumuladas por clase')
plt.xlabel('Clase')
plt.ylabel('Número de personas')
plt.show()
