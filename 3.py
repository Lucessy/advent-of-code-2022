def get_lines():
    '''OBJ = Recoje los datos de un texto y los convierte a una lista'''
    
    lines = open("input3.txt","r").readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
    return lines

lista = get_lines()

import string
def dicAlphabet():
    Alfabeto = {}
    minusculas = list(string.ascii_lowercase)
    j = 1
    for i in minusculas:
        Alfabeto[i] = j
        j += 1

    mayusculas = list(string.ascii_uppercase)
    for i in mayusculas:
        Alfabeto[i] = j
        j += 1
    return Alfabeto


def comparar():

    lista_letras = []

    for i in range(len(lista)):
        
        cadena = []
        cadena += lista[i]
        mitad = int(len(cadena)/2)

        columna1 = cadena[:mitad]
        columna2 = cadena[mitad:]

        for letra1 in columna1:
            if letra1 in columna2:      #En vez de hacer dos "for" hacemos una condicion para la columna2
               #Si está la letra entonces la guardamos y hacemos un break, ya que no necesitamos más letras.
                lista_letras += letra1
                break
    
    return lista_letras

def suma_prioridades():

    lista_letras = comparar()
    suma_total = 0
    alfabeto = dicAlphabet()
    for letra in lista_letras:
        suma_total += alfabeto[letra]
    
    return suma_total

print(suma_prioridades())



        
        

