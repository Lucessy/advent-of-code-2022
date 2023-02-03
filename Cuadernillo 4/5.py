calificaciones = {"Sobresaliente":10-9,"Notable":8-7,"Aprobado":6-5,"Suspenso":4-0}
lista_calif = [0,4,6,7,8,9,10]

posicion = 0
for calificacion in lista_calif:
    nombre = calificaciones[calificacion]
    lugar = lista_calif.index(calificacion)
    lista_calif[lugar] = nombre

print(lista_calif)
