def suma_dos_listas (lista1,lista2):
    '''lista(int),lista(int) -> lista(int)
    OBJ = Suma dos listas de igual longitud creando una nueva lista con la suma de sus numeros
    '''
    long_1 = len(lista1)
    long_2 = len(lista2)
    suma_listas = []
    
    if long_1 == long_2:
        for i in range(long_1):
            suma_listas.append(lista1[i] + lista2[i])
            
    return suma_listas

#Probador
cadena1= [1,2,3,4,5]
cadena2= [0,1,2,3]
print(suma_dos_listas(cadena1,cadena2))

def es_mayor(lista1,lista2):
    long_1 = len(lista1)
    long_2 = len(lista2)
    if long_1 > long_2: 
        lista_mayor = lista1[:]
    else: 
        lista_mayor = lista2[:]
    return lista_mayor

def suma_dos_listas (lista1,lista2):
    '''lista(int),lista(int) -> lista(int)
    OBJ = Suma dos listas creando una nueva lista con la suma de sus numeros
    '''
    long_1 = len(lista1)
    long_2 = len(lista2)
    suma_listas = []
    min_num = min(long_1,long_2)
    
    if long_1 > long_2: 
        lista_mayor = lista1[:]
    else: 
        lista_mayor = lista2[:]

    for i in range(min_num):
        suma_listas.append(lista1[i] + lista2[i])
        
    suma_listas += lista_mayor[min_num:]
    
    return suma_listas

#Probador
cadena1= [1,2,3,4,5,6]
cadena2= [0,1,2,5]
print(suma_dos_listas(cadena1,cadena2))
