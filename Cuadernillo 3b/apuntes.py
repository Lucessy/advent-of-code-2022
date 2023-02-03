#Generar aleatoriamente 10 n´umeros entre 0 y 100 y
#mostrar en pantalla su suma

import random
suma = 0
for i in range(10):
    numero_actual = random.randint(0,100)
    suma += numero_actual
print(f"La suma de los 10 números es: {suma}")

#Obtener el factorial de un número
def factorial (n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

print(factorial(5))


#Mostrar las tablas de multiplicar de los números pares

def tabla_pares (n):
    for i in range(2,n+1,2):
        for j in range(1,11):
            print(i,"x",j,"=",i*j)
        print("---------------")

tabla_pares


#Obtener la siguiente secuencia
n = 4
for i in range(2, n+1):
    sum = 1
    print(sum, end="")
    for j in range(2,i):
        sum = sum + j
        print(" +",j,end="")
    print(" =", sum)

n = 10
while n > -1:
    print(n)
    n = n - 1
print("Despegue!")

import random
inverso = 0
n = random.randint (1 ,1000)
while n % 10 == 0: n //= 10 # elimina ceros finales
print(f"Numero a invertir : {n}")
while (n > 0) :
    inverso *= 10
    inverso += n % 10
    n //= 10
print ("Resultado de invertir sus cifras : ", inverso )


#Calcular la media de todos los n´umeros entre 0 y 100
#aleatoriamente generados hasta que salga un cero

