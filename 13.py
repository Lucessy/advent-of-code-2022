import ast

def GetLines(nombre):
    '''OBJ = Recoge los datos de un texto y los convierte a una lista'''
    
    lines = open('advent of code/inputs/' + nombre + '.txt',"r").readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")

    for pos in lines:
        if pos == '':
            lines.remove(pos)
    return lines

def TransformarLista(linea,input):
    i = 0
    listaTemporal = []
    terminar = False
    numero = 0

    while not terminar:
        
        if linea == '':
            terminar = True

        elif linea[i] == ',':
            linea = linea[1:]

        elif linea[i].isdigit():
            if i+1 < len(linea):
                if linea[i+1].isdigit():
                    numero = linea[i] + linea[i+1]
                    listaTemporal.append(int(numero))
                    linea = linea[2:]
                else:
                    listaTemporal.append(int(linea[i]))
                    linea = linea[1:]
        
            else:
                listaTemporal.append(int(linea[i]))
                linea = linea[1:]
                terminar = True

        elif linea[i] == '[':
            listaTemporal.append(TransformarLista(linea[1:],input))
            listaR = str(listaTemporal[-1]).replace(' ','')
            long = len(listaR)
            linea = linea[long:]
            
        elif linea[i] == ']':
            return listaTemporal
        
    return listaTemporal

def EstaOrdenada(listaIzquierda,listaDerecha):
    '''String -> Bool
    OBJ = Compara dos listas por cada elemento hasta encontrar si el primer elemento es menor
    para que estén en el orden correcto
    '''
    ordenada = None
    i = 0
    
    while ordenada == None:
        if len(listaIzquierda) == len(listaDerecha):
            if listaDerecha == [] and listaIzquierda == []:
                ordenada = None
                return ordenada
            elif listaIzquierda == []:
                ordenada = True
                return ordenada
            elif listaDerecha == []:
                ordenada = False
                return ordenada
            elif len(listaDerecha) == i or len(listaIzquierda) == i:
                return ordenada
        elif len(listaIzquierda) < len(listaDerecha):
            if i == len(listaIzquierda) and ordenada == None:
                ordenada = True
                return ordenada
        elif len(listaIzquierda) > len(listaDerecha):
            if i == len(listaDerecha) and ordenada == None:
                ordenada = False
                return ordenada
        elemIzq = listaIzquierda[i]
        elemDer = listaDerecha[i]
        if type(elemDer) == list and type(elemIzq) == list:
            ordenada = EstaOrdenada(elemIzq,elemDer)
            
        elif type(elemDer) == list and type(elemIzq) == int:
            elemIzqLista = []
            elemIzqLista.append(elemIzq)
            ordenada = EstaOrdenada(elemIzqLista,elemDer)
            
        elif type(elemDer) == int and type(elemIzq) == list:
            elemDerLista = []
            elemDerLista.append(elemDer)
            ordenada = EstaOrdenada(elemIzq,elemDerLista)
            
        else:
            ordenada = EsMayor(elemIzq,elemDer)
        i += 1
    return ordenada
        
def EsMayor(izq,der):
    if izq < der:
        ordenada = True
    elif izq > der:
        ordenada = False
    else:
        ordenada = None
    return ordenada

def ListasOrdenadas(input):
    sumaIndices = 0
    listaTransformada = ListaTransformada(input)
    listaIterable = []
    for i in range(0,len(listaTransformada),2):
        booleana = EstaOrdenada(listaTransformada[i],listaTransformada[i+1])
        listaIterable.append(booleana)
    for i in range(len(listaIterable)):
        if listaIterable[i] == True:
            sumaIndices += i+1
    return sumaIndices

def OrdenCorrecto(v):
    '''Devuelve una lista con los paquetes ordenados utilizando el método
    de la burbuja '''
    
    long = len(v)-1
    for pasada in range(0,long,-1):
        AscenderMenor(v,pasada,long)
        for linea in v:
            print(linea)
        print()
    return v
            
def AscenderMenor(v,primero,ultimo):
    for i in range(ultimo,primero,-1):
            if not EstaOrdenada(v[i-1],v[i]):
                v[i],v[i-1] = v[i-1],v[i]
                

#Metodo de la burbuja
def bubble_sort (v) :
    """ lista -> None
    OBJ : Ordena una lista completa ascendentemente .
    Metodo burbuja . Modifica la lista .
    """
    long = len(v) - 1
    # haremos long - 1 pasadas : 10 elementos -> 9 pasadas
    for pasada in range (0 , long ) :
    # en cada pasada comparamos el elemento i con el i+1
        for i in range (0 , long - pasada ) :
        # cambiamos de posicion si el izquierdo es mayor ,
        #para ordenar ascendente
            if not EstaOrdenada(v[i],v[i+1]):
                v[i] , v[i +1] = v[i+1] , v[i]
            

def ListaTransformada(input):
    listaTransformada = []
    for linea in input:
        linea = linea[1:-1]
        listaTransformada.append(TransformarLista(linea,input))
    return listaTransformada

#Probador
input = GetLines('input13')
v = ListaTransformada(input)
v.append([[6]])
v.append([[2]])
bubble_sort(v)
print((v.index([[2]])+1) * (v.index([[6]])+1))





###########################################

def GetLines2(nombre):
    '''OBJ = Recoge los datos de un texto y los convierte a una lista'''
    
    lines = open('advent of code/inputs/' + nombre + '.txt',"r").readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
        if lines[i] != '': 
            lines[i] = ast.literal_eval(lines[i])
    for pos in lines:
        if pos == '':
            lines.remove(pos)
    return lines

def SonIguales():
    lista2 = GetLines2('input13')
    listaTransformada = []
    for linea in GetLines('input13'):
        linea = linea[1:-1]
        listaTransformada.append(TransformarLista(linea,input))
    for i in range(len(lista2)):
        if lista2[i] != listaTransformada[i]:
            print("The lists are not equal.")
            print(lista2[i],'/',listaTransformada[i])
            break
    else:
        print("The lists are equal.")