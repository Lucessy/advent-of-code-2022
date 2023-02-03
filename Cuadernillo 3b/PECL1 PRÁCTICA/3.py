from unicodedata import decimal

import math
def es_simpatico (num):
    """float -> bool
    OBJ = Determina si la suma de las 3 primeras cifras decimales son iguales a su parte entera, siendo simpático
    PRE = num > 0
    """
    num_entero = int(num)
    decimal_solo = round(num - num_entero,3)
    suma_num_decimales = 0
    for i in range(3):
        suma_num_decimales += int((decimal_solo)*10)
        decimal_solo = round(((decimal_solo)*10)-int((decimal_solo)*10),3)
    if suma_num_decimales == num_entero:        
        print(f"El número: {num}, es simpático")
    else: 
        print(f"El número: {num}, no es simpático")

from unicodedata import decimal

import math
def es_simpatico2 (num):
    """float -> bool
    OBJ = Determina si la suma de las 3 primeras cifras decimales son iguales a su parte entera, siendo simpático
    PRE = num > 0
    """
    num = abs(num)
    num_entero = int(num)
    num_multiplicado = 10
    decimal_solo = round(num - num_entero,3)
    suma_num_decimales = 0
    for i in range(3):
        suma_num_decimales += int((decimal_solo)*num_multiplicado)
        decimal_solo = round(((decimal_solo)*num_multiplicado)-int((decimal_solo)*num_multiplicado),3)
    return suma_num_decimales == num_entero


def es_simpatico3 (num):
    """float -> bool
    """
    num = abs(num)
    numero_entero = int(num)
    numeros_decimales = int((num -numero_entero)* 1000)
    suma_decimales = 0
    for i in range(3):
        suma_decimales += numeros_decimales % 10
        numeros_decimales //= 10
    return suma_decimales == numero_entero


#Probador

num_prueba = 6.321
if es_simpatico3(num_prueba):
    print(f"El número: {num_prueba}, es simpático")
else:
    print(f"El número: {num_prueba}, no es simpático")



def es_simpatico4(n):
    n = abs(n)
    parte_entera = int(n)
    parte_decimal = n - parte_entera
    parte_decimal = int(parte_decimal * 1000)
    suma_cifras_parte_decimal = 0
    while parte_decimal > 0:
        suma_cifras_parte_decimal += parte_decimal % 10
        parte_decimal //= 10
    return suma_cifras_parte_decimal == parte_entera
# probador
numero_prueba = 6.321
if es_simpatico4(numero_prueba): print (f'El número {numero_prueba} es simpático')
else: print (f'El número {numero_prueba} no es simpático')