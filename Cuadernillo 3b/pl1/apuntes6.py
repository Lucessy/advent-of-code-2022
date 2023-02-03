import math

def serie_inf(x,eps):
    """Float, float -> float
    OBJ = Suma de la serie S = 1 + x/1! + x2/2!...
    """
    total_suma = 0
    i = termino = 1
    while (abs(termino) > eps): #Correcto funcionamiento para x < 0
        total_suma += termino
        termino = (x**i)/math.factorial(i)
        i += 1
    return total_suma #Los += son asi xd

print(serie_inf(3,0.0001))