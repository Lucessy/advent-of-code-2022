def mostrar_elementos(lista):
    if len(lista)>0:
        print(lista[0])
        mostrar_elementos(lista[1:])

#Probador
lista=[1,2,3,4,5,6]
mostrar_elementos(lista)
