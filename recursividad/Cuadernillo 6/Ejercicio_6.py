
def cuenta_digitos(num):
    """ int --> int
    OBJ: Cuenta los dígitos de un número dado.
    """
    if num < 10:
        digitos = 1
    else:
        digitos = 1 + cuenta_digitos(num // 10)
    return digitos

# Probador
print(f'El número de dígitos de 9365 es: {cuenta_digitos(9365)}')
