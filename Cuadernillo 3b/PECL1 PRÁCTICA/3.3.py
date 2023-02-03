from re import X


def es_par_casilla(x,y):
    '''int,int -> bool
    '''
    return (x + y) % 2 == 0

def casilla_diagonal_principal (x,y):
    '''int,int -> bool'''
    return x == y

def casilla_diagonal_inversa (x,y,n):
    return x+y == n-1

def tablero(num):
    '''int -> None
    OBJ = Dibuja un cuadrado con los simbolos dados para la diagonal inversa,principal y coordenadas pares e impares'''
    for i in range(num):
        for j in range(num):
            if casilla_diagonal_principal(i,j):
                print("#",end=" ")
            elif casilla_diagonal_inversa(i,j,num):
                print('$',end=" ")
            elif es_par_casilla(i,j):
                print("O",end=" ")
            else:
                print('X',end=" ")
        print('')


#Probador
num = int(input("Introduzca un número entero positivo para la dimensión del tablero:"))
while num < 0:
    num = int(input("Introduzca un número entero >>>>>>POSITIVO<<<<<<, por favor:"))
tablero(num)