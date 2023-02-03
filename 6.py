def get_lines(nombre):
    '''OBJ = Recoje los datos de un texto y los convierte a una lista'''
    
    lines = open("advent of code/inputs/" + nombre + ".txt","r").readline()

        
    return lines


def StartOfPacket(long):

    linea = get_lines("input6")
    lista_letras = []
    num = long
    for simbolo in linea:
        lista_letras.append(simbolo)
        if len(lista_letras) == long:
            iterable = (lista_letras[long-num:].count(elemento) != 1 for elemento in lista_letras[long-num:])
            if any(iterable):
                long += 1
            else:
                break

    return long

print(StartOfPacket(14))

#Función set(): Es como una lista sin elementos repetidos.
#marca = set(lista)
#set = {1,2,'a'}