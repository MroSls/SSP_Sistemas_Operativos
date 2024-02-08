'''Crear un directorio utilizando pandas, (Nombre, Teléfono, Correo, Domicilio) y guardarlo en un archivo CSV.'''
import pandas as pd

datos = {
    'Nombre': ['Juan', 'María', 'Pedro'],
    'Telefono': ['123456789', '987654321', '555555555'],
    'Correo': ['juan@example.com', 'maria@example.com', 'pedro@example.com'],
    'Domicilio': ['Calle 123', 'Avenida 456', 'Plaza 789']
}

# Crear un DataFrame a partir del diccionario
directorio = pd.DataFrame(datos)

# Imprimir el directorio
print(directorio)
# Guardar el directorio en un archivo CSV
directorio.to_csv('Actividades/Practica3/directoriop.csv', index=False)