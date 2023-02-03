import turtle
def dibujar_rectangulo(lado, altura , color):
    """ float -> None
        OBJ: Dibuja un cuadrado en pantalla a partir del punto origen actual
    """
    turtle.color(color)
    turtle.pendown()
    turtle.forward(lado)
    turtle.left(90)
    turtle.forward(altura)
    turtle.left(90)
    turtle.forward(lado)
    turtle.left(90)
    turtle.forward(altura)


dibujar_rectangulo(100 , 200 , "black")