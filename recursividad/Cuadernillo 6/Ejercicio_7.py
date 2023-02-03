
def binario(num):
    """ int --> str
    OBJ: Convierte un número a binario
    """
    resultado = ''
    while num > 0:
        resultado = str(num % 2) + resultado
        num = num // 2
    return resultado

def binario_recursivo(num):
    """ int --> str
    OBJ: Convierte un número a binario recursivamente
    """
    if num == 0:
        resultado = ''
    else:
        resultado = binario_recursivo(num // 2) + str(num % 2)
    return resultado

# Probador
print(f'El número 5 en binario es: {binario(5)}')
print(f'El número 5 en binario_recursivo es: {binario_recursivo(5)}')
