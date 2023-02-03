
suma_anterior = 0
suma_actual = 0
mayor = 0

with open("ejemplo.txt", mode = "r") as input:
    for linea in input:
        if linea != "\n":
            suma_actual += int(linea)
        else:
            if suma_actual > suma_anterior:
                mayor = suma_actual
                suma_anterior = suma_actual
                suma_actual = 0
            else:
                suma_actual = 0
    print(mayor)

    



suma_anterior = 0
suma_actual = 0
mayor = 0
bloque = 0
bloque_anterior = 0

with open("input.txt", mode = "r") as input:
    for linea in input:
        if linea != "\n":
            suma_actual += int(linea)
        else:
            bloque += 1
            if suma_actual > suma_anterior:
                bloque_anterior =  bloque
                mayor = suma_actual
                suma_anterior = suma_actual
                suma_actual = 0
            else:
                suma_actual = 0
    print(f"El bloque mayor es: {bloque_anterior} con un total de: {mayor}")
