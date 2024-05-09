# Construir una función reciba el fichero bancos.csv y cree un diagrama de líneas
# con las series temporales de las cotizaciones de cierre de cada banco.
import matplotlib.pyplot as plt
import pandas as pd

file = 'Actividades/Practica10/CSV/bancos.csv'
def crear_grafico_lineas(fichero_csv):
  # Lectura de los datos del fichero CSV
  datos = pd.read_csv(fichero_csv, index_col="Fecha", parse_dates=True)

  # Creación del diagrama de líneas
  plt.figure(figsize=(10, 6))
  for banco, cotizaciones in datos.items():
    plt.plot(cotizaciones, label=banco)
  plt.xlabel("Fecha")
  plt.ylabel("Cotización de cierre")
  plt.title("Series temporales de cotizaciones de cierre por banco")
  plt.legend()
  plt.grid(True)

  # Visualización del gráfico
  plt.show()

# Ejemplo de uso
crear_grafico_lineas(file)
