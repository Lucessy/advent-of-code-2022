def varianza_poblacion (p0,pmedia,n):
    varianza = 0
    for i in range (n):
        varianza += (p0-pmedia)**2/(n-1)
    return varianza

print(varianza_poblacion(100,150,50))
