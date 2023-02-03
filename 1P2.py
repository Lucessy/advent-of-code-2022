lista = []
suma_actual = 0
with open("input.txt", mode = "r") as input:
    for linea in input:
        if linea != "\n":
            suma_actual += int(linea)
        else:
            lista.append(suma_actual)
            lista.sort(reverse = True)
            suma_actual = 0
    lista.append(suma_actual)
    lista.sort(reverse = True)
    suma_total = lista[0]+lista[1]+lista[2]
    print(suma_total)

def top_calorias():

    calorias = []
    suma_actual = 0
    with open("input.txt", mode = "r") as input:
        for linea in input:
            if linea != "\n":
                suma_actual += int(linea)
            else:
                calorias.append(suma_actual)
                calorias.sort(reverse = True)
                suma_actual = 0
    calorias.append(suma_actual)
    calorias.sort(reverse = True)
    suma_total = lista[0]+lista[1]+lista[2]
    return suma_total

print(top_calorias())