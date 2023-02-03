def get_lines():
    '''OBJ = Recoje los datos de un texto y los convierte a una lista'''
    
    lines = open("input3(2).txt","r").readlines()
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

    lista_total = []

    for i in range(0,len(lista),3):
        
        cadena = cadena1 = cadena2 = []
        cadena1 = lista[i]
        cadena2 = lista[i+1]
        cadena3= lista[i+2]

        for letra1 in cadena1:
            if letra1 in cadena2 and letra1 in cadena3:
                lista_total += letra1
                break

    return lista_total

def suma_prioridades():

    lista_letras = comparar()
    suma_total = 0
    alfabeto = dicAlphabet()
    for letra in lista_letras:
        suma_total += alfabeto[letra]
    
    return suma_total

print(suma_prioridades())