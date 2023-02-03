def dibujar_cuadrado (tamaño):
    """int -> None
    OBJ = Dibujar un cuadrado de "#" con una diagonal númerica.
    PRE = tamaño > 0
    """
    for i in range(tamaño):
        print("#"*i,end="")
        print(i+1,end="")
        for j in range(1,tamaño-i):
            print("#",end="")
        print()


def dibujar_cuadrado2 (tamaño,simbolo,numero_inicio):
    """int -> None
    OBJ = Dibujar un cuadrado de "#" con una diagonal númerica.
    PRE = tamaño > 0
    """
    for i in range(tamaño):
        print(simbolo*i,end="")
        print(numero_inicio," ",end="")
        numero_inicio += 1
        for j in range(1,tamaño-i):
            print(simbolo," ",end="")
        print()

def dibujar_cuadrado3 (tamaño,simbolo,num_inicial):
    """int -> None
    OBJ = Dibujar un cuadrado de "#" con una diagonal númerica.
    PRE = tamaño > 0
    """
    for i in range(tamaño):
        for j in range(tamaño):
            if i==j: 
                print(i+num_inicial,end=" ")
            else: print(simbolo,end=" ")
        print()

#Probador

dibujar_cuadrado3(4,"=",3)