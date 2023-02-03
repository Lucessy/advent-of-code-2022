def esbisiesto (x):
    """ int -> bool
    OBJ: Calcular si un año es bisiesto
    PRE: x >= 0"""
    return x % 4 == 0 and not x % 100 == 0 or x % 100 == 0 and x % 400 == 0

#   Probador
import random
ano = random.randint (0, 2022)
print(f'El año {ano} ¿es bisiesto?: {esbisiesto(ano)}')