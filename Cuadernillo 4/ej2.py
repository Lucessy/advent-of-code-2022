from sys import ps1


def valor_maximo_lista (lista1,lista2):
    '''list,list -> float
    OBJ = Calcula el valor maximo de la lista
    '''
    suma_lista1 = peso(lista1)
    suma_lista2 = peso(lista2)
    if suma_lista1 > suma_lista2:
    return suma_lista1
    else:
    return suma_lista2
    return max(suma_lista1,suma_lista2)
    

def peso(lista):
    peso = 0
    for elemento in lista:
        peso += abs(elemento)
    return peso


