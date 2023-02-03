def calificacion (nota):
    if 0 <= nota <= 5:
        nota_texto = "Suspenso"
    elif 5<=nota<=6.5:
        nota_texto = "Aprobado"
    elif 6.5<=nota<=8.5:
        nota_texto = "Notable"
    else:
        nota_texto = "Sobresaliente"
    return nota_texto

#Probador
print(calificacion(8))