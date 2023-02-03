def get_lines(nombre):
    '''OBJ = Recoge los datos de un texto y los convierte a una lista'''
    
    lines = open('advent of code/inputs/' + nombre ,"r").readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
    return lines


from collections import defaultdict

def columnas():
    diccionario = defaultdict(list)
    lista = get_lines('ejemplo5.txt')
    
    for i in range(len(lista),0,-1):
        num = 1
        for j in range(0,len(lista[i-1]),4):
            
            if lista[i-1][j] != " ":
                diccionario[num].append(lista[i-1][j+1])
                num += 1
            else:
                num += 1

    return diccionario

dicc = columnas()

#dicc = {1 : ['[F]','[T]','[C]',''],2 : ['[M]','[C]','[D]'] ,3 : ['[P]']}

def instrucciones(nombre):

    instrucciones = get_lines("input5.txt")

    for i in range(len(instrucciones)):
        instrucciones[i] = instrucciones[i].replace("move ","")
        instrucciones[i] = instrucciones[i].replace(" from ",",")
        instrucciones[i] = instrucciones[i].replace(" to ",",")
    
    for linea in instrucciones:
        instruccion = []
        lista_nueva = linea.split(",")

        for simbolo in lista_nueva:
            simbolo = int(simbolo)
            instruccion.append(simbolo) 
                
        if nombre == '9000':
            for veces in range(instruccion[0]):

                columna = dicc[instruccion[1]]
                longitud = len(columna)
                valor = columna[(longitud-1)]
                del columna[(longitud-1)]
                dicc[instruccion[2]].append(valor)
        
        else:
            if instruccion[0] == 1:
                columna = dicc[instruccion[1]]
                valor = columna[-1]
                del columna[-1]
                dicc[instruccion[2]].append(valor)

            else:
                for veces in range(instruccion[0],0,-1):

                    columna = dicc[instruccion[1]]
                    longitud = len(columna)
                    valor = columna[longitud - veces]
                    del columna[longitud - veces]
                    dicc[instruccion[2]].append(valor)
                    print(dicc)
    
    for key in dicc:
        print(end=dicc[key][-1])
    print("")
    return dicc
        

print(instrucciones("9001"))
