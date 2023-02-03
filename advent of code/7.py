def GetLines(nombre):
    '''OBJ = Recoge los datos de un texto y los convierte a una lista'''
    
    lines = open("advent of code/inputs/" + nombre + ".txt","r").readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
    return lines

def Ruta(nombre):
    '''OBJ = Devuelve un diccionario con el peso total de todos los
    directorios'''
    input = GetLines(nombre)
    ruta = {}
    linea = 0
    path = []
    no_Final = True
    while linea < len(input):

        lineaActual = input[linea]
        if '$ cd ..' not in lineaActual:
            suma_archivos = 0
            directorio = lineaActual.removeprefix('$ cd ')
            path.append(directorio)
            linea += 2
            lineaActual = input[linea]
            
            while '$ cd' not in lineaActual and no_Final:
                
                if lineaActual[0].isdigit():
                    numero = ''
                    for i in range(len(lineaActual)):
                        if lineaActual[i] == ' ':
                            break
                        else:
                            numero += lineaActual[i]
                    suma_archivos +=  int(numero)

                linea += 1
                if linea != len(input):
                    lineaActual = input[linea]
                else:
                    no_Final = False
            
            ruta_str = ','.join(path)
            ruta[ruta_str] = suma_archivos
            if len(ruta_str) != 1:
                pathTempo = []
                i = 0
                while len(pathTempo) != 1:
                    pathTempo = path[:-1-(i)]
                    ruta_str = ','.join(pathTempo)
                    ruta[ruta_str] += suma_archivos
                    i += 1

        else:
            path = path[:-1]
            linea += 1

    return ruta

def Suma(limite):
    suma_total = 0
    dicc = Ruta('input7')
    for key in dicc:
        if dicc[key] <= limite:
            suma_total += dicc[key]
    return suma_total

def DeleteMinDirectory():
    dicc = Ruta('input7')
    espacioNecesarioRestante = 30000000 - (70000000 - dicc['/'])
    valores = []
    for key in dicc:
        if dicc[key] >= espacioNecesarioRestante:
            valores.append(dicc[key])
    minimo_peso = min(valores)

    return minimo_peso

print(Ruta('input7'))
print(Suma(100000))
