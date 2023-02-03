import math
def serie_s (n):
    '''OBJ = Calcula el valor de la serie S para un valor determinado "n"
    PRE = n > 0'''
    suma_serie = 0
    for i in range(1,n+1):
        suma_serie += termino(i)
    return suma_serie

def termino(n):
    return (n)*(-1)**(n+1)/math.factorial(n-1)

numero = 1
suma_serie = serie_s(numero)
while abs(suma_serie) >= 1e-15:
    numero += 1
    suma_serie += termino(numero)
    
print("A partir del término",numero,"La serie es menor que 1e-15")

print(serie_s(1))