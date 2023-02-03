def suma_lista(lista):
    if lista==[]:
        resultado = 0
    else:
        resultado = lista[0] + suma_lista(lista[1:])
    return resultado

#probador
lista = [1,2,3,3,4]
print(suma_lista(lista))