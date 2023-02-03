import random
def lista_enteros(limite):
    lista_enteros = []
    media = 0

    for i in range(limite):
        numero =  random.randint(0,100)
        lista_enteros.append(numero)
        media += numero
        
    lista_enteros.sort()
    media_total = media / limite
    minimo = lista_enteros[0]
    maximo = lista_enteros[limite-1]

    return minimo,maximo,media_total


print("minimo/maximo/media:\n",lista_enteros(20))
