def superficie_regalo (largo,ancho,alto):
    '''int, int, int -> 
    OBJ = Calcula la superficie necesaria para envolver un regalo más un extra que es el área del lado más pequeño.
    PRE = 0 < largo,ancho,alto
    '''
    superficie = 2*(largo*ancho) + 2*(ancho*alto) + 2*(alto*largo)
    menor = min(largo,ancho,alto)
    extra = menor * menor
    print(f"Se necesitan: {superficie+extra} cm2 en total para envolver el regalo, superficie: {superficie} cm2, extra: {extra} cm2")
    return superficie + extra
superficie_regalo(1,1,10)