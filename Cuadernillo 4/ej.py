lista = [1,2,3,4,5,6,7,8,9,10]
def cantidad_impar (lista):
    '''lista -> int
    OBJ = retorna la cantidad de números impares en una lista'''
    cantidad = 0
    for numero in lista:
        if numero % 2 != 0: 
            cantidad += 1
    return cantidad

print(cantidad_impar(lista))
