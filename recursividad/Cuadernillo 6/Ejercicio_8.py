
def suma_pares(num):
    """ int -> int
    OBJ: Suma todos los pares anteriores a num.
    PRE: n >= 0 """
    if num % 2 == 1:
        num -= 1
    if num == 0:
        suma = 0
    else:
        suma = num + suma_pares(num - 2)
    return suma

# Probador
print(f'La suma de los pares anteriores a 11 es: {suma_pares(11)}')
