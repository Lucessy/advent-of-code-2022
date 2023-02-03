def parejas_que_cumplen(altitudes,distancias,objetivo,error):
    '''lista(int),lista(int),float,float -> None
    OBJ = Calcular las parejas de altitud-distancia que quedaron más cerca del valor objetivo junto con el margen de error
    PRE = 0 < '''
    max = objetivo + error
    min = objetivo - error
    num_pares = 0
    cadena_resultante = ""
    print("La(s) pareja(s) que cumple(n) cuya suma quedó cerca del objetivo:",end="")

    for altitud in altitudes:
        for distancia in distancias:
            suma_parejas = altitud + distancia
            if min <= suma_parejas <= max:
                cadena_resultante += (f"({altitud},{distancia}) ")
                num_pares += 1      
    print(cadena_resultante)
    print("Número de pareja(s):",num_pares)

altitud = [1725, 979, 299, 495, 1826] 
distancia =  [101, 1725, 366, 111 , 299]
objetivo = 2020.0
error = 5.5
parejas_que_cumplen(altitud,distancia,objetivo,error )


        
