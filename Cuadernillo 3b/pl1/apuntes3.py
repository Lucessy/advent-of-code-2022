def imprimir_triangulo(n):
    """Int -> None
    OBJ = Imprime un tringulo numerico
    PRE = n > 0
    """
    for i in range(n):
        for j in range(i+1, n+1):
            print(j,end=" ")
        print()

imprimir_triangulo(6)