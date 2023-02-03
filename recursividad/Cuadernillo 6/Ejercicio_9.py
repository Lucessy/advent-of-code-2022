
def alumno(nombre, edad, titulacion):
    """ str, int, str -> dict
    OBJ: Devuelve un diccionario con los datos de un alumno.
    """
    return {"nombre": nombre, "edad": edad, "titulacion": titulacion}

def sumar_edades(lista):
    """ list --> int
    OBJ: Suma recursivamente las edades de los alumnos.
    """
    if len(lista) == 0:
        suma = 0
    else:
        suma = lista[0]['edad'] + sumar_edades(lista[1:])
    return suma

# Programa
lista_alumnos = [
    alumno('Álvaro', 30, 'Informática'),
    alumno('Carlos', 20, 'Informática'),
    alumno('Manuel', 23, 'Informática'),
    alumno('María', 18, 'Informática'),
    alumno('Lucía', 25, 'Informática')
]
print(lista_alumnos)
print(sumar_edades(lista_alumnos))
