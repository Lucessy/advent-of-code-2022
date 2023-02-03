def lista_par_impar(lista_enteros):
    '''list(int) -> list(int),list(int)
    OBJ = Devuelve dos cadenas una con pares y otra con impares dado un orden determinado'''

    lista_pares = []
    lista_impares = []

    for numero in lista_enteros:
        if numero % 2 == 0:
            lista_pares.append(numero)
            lista_pares.sort()
        else:
            lista_impares.append(numero)
            lista_impares.sort(reverse=True)

    return lista_pares,lista_impares


#Probador
lista_enteros = [0,1,2,3,4,5,6,7,8,9]
print(lista_par_impar(lista_enteros))