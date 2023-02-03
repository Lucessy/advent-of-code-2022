def get_lines():
    '''OBJ = Recoje los datos de un texto y los convierte a una lista'''
    
    lines = open("input4.txt","r").readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
    return lines

lista_pares = get_lines()

def primer_par():
    primer_par = []
    for linea in lista_pares:
        posicion_coma = 0
        posicion_guion = 0
        for simbolo in linea:
            if simbolo != ",":
                posicion_coma += 1
            else:
                break
        for simbolo in linea:
            if simbolo != "-":
                posicion_guion += 1
            else:
                break
        
        primer_numero = linea[:posicion_guion]
        primer_numero = int(primer_numero)
        segundo_numero = linea[posicion_guion+1:posicion_coma]
        segundo_numero = int(segundo_numero)
        
        primer_par.append(primer_numero)
        primer_par.append(segundo_numero)

    return primer_par
        
def segundo_par():
    segundo_par = []
    for linea in lista_pares:
        posicion_coma = 0
        for simbolo in linea:
            if simbolo != ",":
                posicion_coma += 1
            else:
                break
        linea_temp = linea[posicion_coma+1:]
        posicion_guion = 0
        for simbolo in linea_temp:
            if simbolo != "-":
                posicion_guion += 1
            else:
                break
        
        primer_numero = linea_temp[:posicion_guion]
        primer_numero = int(primer_numero)
        segundo_numero = linea_temp[posicion_guion+1:]
        segundo_numero = int(segundo_numero)
        
        segundo_par.append(primer_numero)
        segundo_par.append(segundo_numero)

    return segundo_par

def comparar():
    
    par1 = primer_par()
    par2 = segundo_par()
    numero_total = 0
    total_overlap = 0

    for i in range(0,len(par1),2):
        numero1_1 = par1[i]
        numero2_1 = par1[i+1]
        lista_completa_1 = []
        for j in range(numero1_1,numero2_1+1):
            lista_completa_1.append(j)
        
        numero1_2 = par2[i]
        numero2_2 = par2[i+1]
        lista_completa_2 = []
        for j in range(numero1_2,numero2_2+1):
            lista_completa_2.append(j)

        numero_comun = 0
        overlap = 0

        for numero in lista_completa_1:
            if numero in lista_completa_2:
                overlap = 1
                break
        
        total_overlap += overlap

        if len(lista_completa_1) == len(lista_completa_2):
            for numero in lista_completa_1:
                if numero in lista_completa_2:
                    numero_comun = 1
                else:
                    numero_comun = 0
                    break
        else:
            minimo = min(len(lista_completa_1),len(lista_completa_2))
            if minimo == len(lista_completa_1):
                lista_pequeña = lista_completa_1
                lista_grande = lista_completa_2
                for numero in lista_pequeña:
                    if numero in lista_grande:
                        numero_comun = 1
                    else:
                        numero_comun = 0
                        break
            else:
                lista_pequeña = lista_completa_2
                lista_grande = lista_completa_1
                for numero in lista_pequeña:
                    if numero in lista_grande:
                        numero_comun = 1
                    else:
                        numero_comun = 0
                        break

        numero_total += numero_comun
        
    return numero_total, total_overlap

print(comparar())
