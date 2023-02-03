
import random
def suma_numero():
    suma_numeros = 0
    for i in range(10):
        num = random.randit(1,15)
        if num % 2 == 0:
            suma_numeros += num
    return suma_numeros


def es_par(n):
    return n % 2 == 0

def es_primo(n):
    primo = True
    i = n-1
    while i > 1:
        if n % i == 0:
            primo = False
        i -= 1
    return primo

def es_multiplo(n,m):
    return n % m == 0

suma_primos = numeros_primo = 0
numero_minimo = 10
numero_maximo = 25
menor = 1
mayor = 15
cantidad_numeros = random.randint(numero_minimo,numero_maximo)
for numero in range(cantidad_numeros):
    numero = random.randint(menor,mayor)
    if es_primo(numero):
        suma_primos += numero
        numeros_primo += 1
if numeros_primo > 0:
    print("La media de los número primos es:",suma_primos / numeros_primo)
else:
    print("No se generó ningún número primo")

numero_multiplos = 0
respuesta = "SI"
while respuesta != "NO":
    num = random.randint(menor,mayor)
    if es_multiplo(num,3) or es_multiplo(num,7):
        numero_multiplos +=1
    respuesta = input("¿Desea Continuar (SI/NO)?:") 
print("El número de multiplos de 7 y 3 son:",numero_multiplos)



