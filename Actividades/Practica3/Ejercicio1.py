'''Crear un directorio utilizando pandas, (Nombre, Teléfono, Correo, Domicilio) y guardarlo en un archivo CSV.'''
import pandas as pd
import re

csv = 'Actividades/Practica3/directorio.csv'
regex_correo=('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
regex_domicilio=('^[a-zA-Z0-9\s]+$')
regex_telefono=('^\\d{10}$')

def ingreso():
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el teléfono: ")
    correo = input("Ingrese el correo: ")
    domicilio = input("Ingrese el domicilio: ")
    validar(nombre, telefono, correo, domicilio)

def validar(Nombre, Telefono, Correo, Domicilio):
    if Nombre.isalpha() and Telefono.isdigit() and re.match(regex_telefono, Telefono) and re.match(regex_correo, Correo) and re.match(regex_domicilio, Domicilio):
        print("Datos válidos")
        diccionario(Nombre, Telefono, Correo, Domicilio)
    else:
        print("Algun dato no es válido\nPor favor, ingrese los datos nuevamente")
        ingreso()

def diccionario(nombre, telefono, correo, domicilio):
    datos = {
        "Nombre": [nombre],
        "Telefono": [telefono],
        "Correo": [correo],
        "Domicilio": [domicilio]
    }
    df = pd.DataFrame(datos)
    archivo(df)


def archivo(df):
    try:
        df_existente = pd.read_csv(csv)
        df_final = pd.concat([df_existente, df])
    except FileNotFoundError:
        df_final = df

    df_final.to_csv(csv, index=False)

ingreso()
