
def esta_en_lista(lista, num):
    """ list, num --> bool
    OBJ: Comprueba si un número está en la lista.
    """
    if len(lista) == 0:
        esta = False
    elif lista[0] == num:
        esta = True
    else:
        esta = esta_en_lista(lista[1:], num)
    return esta

# Probador
print(esta_en_lista([1,2,7,5,3], 5))
print(esta_en_lista([1,2,7,5,3], 4))
