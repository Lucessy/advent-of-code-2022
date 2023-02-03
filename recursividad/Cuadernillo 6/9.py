def SumaEdades(Lista):
    if Lista == []:
        suma = 0
    else:
        suma = Lista[1] + SumaEdades(Lista[3:])
    return suma
