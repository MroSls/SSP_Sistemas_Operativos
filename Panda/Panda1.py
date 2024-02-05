import pandas as pd

Lista_alumnos = pd.DataFrame({
    'Nombre': ['Juan', 'Pedro', 'Maria', 'Luis'],
    'Apellido': ['Lopez', 'Jimenez', 'Perez', 'Gonzalez'],
    'Edad': [18, 21, 25, 19],
    'Carrera' : ['Abogado', 'Ingenieria', 'Medicina', 'Contabilidad']
})

print(Lista_alumnos)

Lista_alumnos1 = pd.DataFrame([
    ['Juan', 'Lopez', 18, 'Abogado'],
    ['Pedro', 'Jimenez', 21, 'Ingenieria']
    ], columns=['Nombre', 'Apellido', 'Edad', 'Carrera'])

print(Lista_alumnos1)