def es_numero_trino (n):
    '''int -> bool
    OBJ = Verifica si un número dado es trino
    PRE = n > 0'''
    m = abs(n)
    if n < 10:
        return False
    else:
        aun_es_trino = True
        cifra_anterior = m % 10
        m //= 10
        while m > 0 and aun_es_trino:
            cifra_actual = m % 10
            if abs(cifra_anterior - cifra_actual) != 3:
                aun_es_trino = False
            else:
                cifra_anterior = cifra_actual
                m //= 10
        return aun_es_trino

def suma_impares_siguientes (x,n):
    '''int,int -> None'''
    if x % 2 != 0:
        suma = x+2
        print(suma,end=" +")
        for i in range(n-1):
            suma += 2
            if i == n-2: print(suma,end=" =",)
            else: print(suma,end=" +")
    else:
        suma = x+1
        print(suma,end=" +")
        for j in range(n-1):
            suma += 2
            if i == n-2: print(suma,end=" =")
            else: print(suma,end=" +")
        

def leer_tres_numeros():
    numero = int(input("Introduzca un número:"))
    while not 99<numero<1000:
        numero = int(input("Error. Introduzca un número de 3 cifras:"))
    return numero

#Probador
num = leer_tres_numeros()
while not es_numero_trino(num):
    num = int(input("Oops. Intenta de nuevo:"))
print("Acaba de introducir un número trino. Su valor es:",num)
if num % 2 == 0: num += 1
else: num += 2
suma_total = num
print("Suma de los 3 impares siguientes:",num,end="")
for i in range (2):
    num += 2
    suma_total += num
    print(" +",num,end="")
print(" =",suma_total)
