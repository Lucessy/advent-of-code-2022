def son_todos_pares (lista):
    '''Pre: len(lista) > 0'''
    if len(lista) == 1:
        return lista[0] % 2 == 0
    else:
        if lista[0] % 2 != 0:
            return False
        else:
            return son_todos_pares(lista[1:])

#Probador
print(son_todos_pares([2,2,4,5]))