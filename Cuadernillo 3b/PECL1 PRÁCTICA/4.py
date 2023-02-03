def es_domino (secuencia):
    """lista(int)-> bool
    OBJ = Verifica si una secuencia cumple con la colocación de las fichas de dominó
    PRE = valores entre 0 y 6, no vacía
    """
    
    longitud_lista = len(secuencia) 
    #Lista no puede ser 0 o impar.
    if longitud_lista == 0 or longitud_lista % 2 != 0:
        return False
    #Si la lista tiene un par, es correcta.
    elif longitud_lista == 2:
        return True  
    #La lista tiene que contener números entre 0 y 6.
    for i in secuencia:
        if i < 0 or i > 6:
            return False
    #Comenzamos con la posición 0 de la lista.
    posicion = 0
    num_inicial = num_final = 0
    for numero in secuencia:
        if posicion > 0:
            if posicion % 2 != 0:
                num_final = numero
            else:
                num_inicial = numero
                if num_final != num_inicial:
                    return False
        posicion += 1
    return True



#Probador
#        0,1,2,3,4,5
lista = [1,2,3]
if es_domino(lista):
    print(f"La secuencia: {lista}, es dominó")
else:
    print(f"La secuencia: {lista}, no es dominó")

