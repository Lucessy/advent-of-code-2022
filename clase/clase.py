def GetLines():
    '''OBJ = Recoge los datos de un texto y los convierte a una lista'''
    
    lines = open("clase/bitcoin.txt","r").readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
    return lines

def Moneda():
    input = GetLines()
    cadenaMonedas = input[0]
    cadenaMonedas = cadenaMonedas.split(":")
    diccMonedas = {}
    del cadenaMonedas[-1]
    for valor in range(0,len(cadenaMonedas),2):
        diccMonedas[cadenaMonedas[valor]] = cadenaMonedas[valor+1]
    return diccMonedas

def Transaccion():
    input = GetLines()
    total = 0
    suma_temp = 0
    diccMoneda = Moneda()
    for linea1 in range(1,len(input)):

        lineaActual = input[linea1].split(':')
        del lineaActual[-1]
        lineaTempo = lineaActual[1:]
        long = len(lineaTempo)

        if int(lineaActual[0]) == long:
            
            for linea in lineaTempo:
                linea = linea.split('-')
                suma_temp += float(linea[0]) * float(diccMoneda[linea[1]])
            total += suma_temp
            print(f'Transacción {linea1}: OK - {round(suma_temp,2)}EUR')
        else:
            print(f'Transacción {linea1}: error')

    return total
print(f'TOTAL: {round(Transaccion(),2)}EUR')
