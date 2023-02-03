def get_lines(nombre):
    '''OBJ = Recoge los datos de un texto y los convierte a una lista'''
    
    lines = open('advent of code/inputs/' + nombre + '.txt',"r").readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
    return lines


def SeñalDelCicloMax(max_ciclo,input):

    x = 1
    ciclo = 1
    for linea in input:
        if linea == 'noop':
            ciclo += 1
        elif ciclo+2 <= max_ciclo:
            valor = int(linea.removeprefix('addx '))
            x += valor
            ciclo += 2
        else:
            break
    
    return x * max_ciclo

def SumaSeñal():
    sumaTotal = 0
    for i in range(20,220+1,40):
        sumaTotal += SeñalDelCicloMax(i)
    return sumaTotal

def ListaCiclosCRT(input):
    '''String -> List(str)
    OBJ = Devuelve una lista con cada ciclo de 40 de lo que dibuja la señal CRT a la string de la 'sprite' horizontal'''
    x = 1
    CRT = ''
    CRTPosicion = 0
    spritePosicion = '###.....................................'
    CRTLista = []

    for linea in input:
        
        if linea == 'noop':

            if CRTPosicion < 40:
                CRT += spritePosicion[CRTPosicion]
                CRTPosicion += 1

                if CRTPosicion == 40:
                    CRTLista.append(CRT)
                    CRTPosicion = 0
                    CRT = ''

            else:
                CRTLista.append(CRT)
                CRTPosicion = 0
                CRT = ''
                CRT += spritePosicion[CRTPosicion]
                CRTPosicion += 1
       
        else:
            valor = int(linea.removeprefix('addx '))
            if CRTPosicion == 40:
                CRTLista.append(CRT)
                CRTPosicion = 0
                CRT = ''
                CRT += spritePosicion[CRTPosicion]
                CRT += spritePosicion[CRTPosicion+1]
            
            elif CRTPosicion == 39:
                CRT += spritePosicion[CRTPosicion]
                CRTLista.append(CRT)
                CRTPosicion = 0
                CRT = ''
                CRT += spritePosicion[CRTPosicion+1]
                
            else:
                CRT += spritePosicion[CRTPosicion]
                CRT += spritePosicion[CRTPosicion+1]
                
            CRTPosicion += 2
            x += valor
            spritePosicion = ''
            for i in range(40):
                if x-1 <= i <= x+1:
                    spritePosicion += '#'
                else:
                    spritePosicion += '.'
            
    return CRTLista

#Probador
input = get_lines('input10')
listaCiclos = ListaCiclosCRT(input)

for linea in listaCiclos:
    for simbolo in linea:
        if simbolo == '#':
            print(end='⚫')
        else:
            print(end=simbolo + ' ')
    print()

