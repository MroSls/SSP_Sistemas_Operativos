import pandas as pd
import matplotlib.pyplot as plt

def graficar_cotizaciones(archivo_csv):
  df_datos = pd.read_csv(archivo_csv)
  df_datos["Fecha"] = pd.to_datetime(df_datos["Fecha"])
  fig, ax = plt.subplots()
  df_datos.groupby('Empresa').plot(x = 'Fecha', y = 'Cierre', ax = ax)
  plt.title('Evolución de las cotizaciones de cierre')
  plt.legend(df_datos.groupby('Empresa').groups.keys())
  plt.show()
graficar_cotizaciones('Actividades/Practica4/bancos.csv')
