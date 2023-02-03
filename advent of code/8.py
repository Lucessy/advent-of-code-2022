def GetLines(nombre):
    '''OBJ = Recoge los datos de un texto y los convierte a una lista'''
    
    lines = open("advent of code/inputs/" + nombre + ".txt","r").readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
    return lines

def Visible(nombre):
    '''OBJ = Devuelve el número de árboles visibles desde 
    el exterior'''
    input = GetLines(nombre)
    visible = 0
    VERTICAL = len(input)
    HORIZONTAL = len(input[0])

    for linea in range(1,VERTICAL-1):
        lineaActual = input[linea]
        for arbol in range(1,HORIZONTAL-1):
            for izquierda in range(0,arbol):
                arbolIzquierda = int(lineaActual[izquierda])
                if arbolIzquierda >= int(lineaActual[arbol]):
                    Izquierda = False
                    break
                else:
                    Izquierda = True
            for derecha in range(HORIZONTAL-1,arbol,-1):
                arbolDerecha = int(lineaActual[derecha])
                if arbolDerecha >= int(lineaActual[arbol]):
                    Derecha = False
                    break
                else:
                    Derecha = True
            
            for arriba in range(0,linea):
                arbolArriba = int(input[arriba][arbol])
                if arbolArriba >= int(lineaActual[arbol]):
                    Arriba = False
                    break
                else:
                    Arriba = True
            
            for abajo in range(VERTICAL-1,linea,-1):
                arbolAbajo = int(input[abajo][arbol])
                if arbolAbajo >= int(lineaActual[arbol]):
                    Abajo = False
                    break
                else:
                    Abajo = True
            
            if Abajo or Arriba or Derecha or Izquierda:
                visible += 1
    exterior = (HORIZONTAL * 2) + ((VERTICAL-2)*2)
    return visible+exterior

print(Visible('input8'))


def arriba(linea,arbol,lineaActual,input):
    Arriba = 0
    
    for arriba in range(linea-1,-1,-1):
            arbolArriba = int(input[arriba][arbol])
            if arbolArriba >= int(lineaActual[arbol]):
                Arriba += 1
                break
            else:
                Arriba += 1

    return Arriba

def abajo(linea,arbol,lineaActual,VERTICAL,input):
    Abajo = 0
    
    for abajo in range((linea+1),(VERTICAL)):
            arbolAbajo = int(input[abajo][arbol])
            if arbolAbajo >= int(lineaActual[arbol]):
                Abajo += 1
                break
            else:
                Abajo += 1
    
    return Abajo

def derecha(arbol,lineaActual,HORIZONTAL):
    Derecha = 0
    
    for derecha in range(arbol+1,HORIZONTAL):
            arbolDerecha = int(lineaActual[derecha])
            if arbolDerecha >= int(lineaActual[arbol]):
                Derecha += 1
                break
            else:
                Derecha += 1

    return Derecha

def izquierda(arbol,lineaActual):
    Izquierda = 0
    for arbol1 in range(arbol-1,-1,-1):
        
            arbolIzquierda = int(lineaActual[arbol1])
            if arbolIzquierda >= int(lineaActual[arbol]):
                Izquierda += 1
                break
            else:
                Izquierda += 1
   
    return Izquierda

def HighScore(nombre):
    '''OBJ = Devuelve el valor máximo  de las multiplicaciones de vistas de un arbol en determinado'''
    input = GetLines(nombre)
    VERTICAL = len(input)
    HORIZONTAL = len(input[0])
    scoreVisible = []

    for linea in range(VERTICAL):
        lineaActual = input[linea]
        for arbol in range(HORIZONTAL):
            
            if linea == 0 or arbol == 0 or linea ==  (VERTICAL-1) or arbol == (HORIZONTAL-1):
                pass

            else:

                Derecha = derecha(arbol,lineaActual,HORIZONTAL)
                Izquierda = izquierda(arbol,lineaActual)
                Arriba = arriba(linea,arbol,lineaActual,input)
                Abajo = abajo(linea,arbol,lineaActual,VERTICAL,input)

                scoreVisible.append(Derecha * Izquierda * Arriba * Abajo)
    
    highScore = max(scoreVisible)
    return highScore

print(HighScore('input8'))