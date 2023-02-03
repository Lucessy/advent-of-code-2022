
def invertir_cadena(cadena):
    """ str --> str
    OBJ: Invierte la cadena de forma recursiva
    """
    if len(cadena) == 0:
        resultado = ''
    else:
        resultado = invertir_cadena(cadena[1:]) + cadena[0]
    return resultado

# Probador
print(invertir_cadena('patata'))
