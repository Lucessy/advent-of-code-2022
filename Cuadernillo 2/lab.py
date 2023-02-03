import turtle
def dibujar_rectangulo(lado, altura):
    """ float -> None
        OBJ: Dibuja un cuadrado en pantalla a partir del punto origen actual
    """
    turtle.pendown()
    turtle.forward(lado)
    turtle.left(90)
    turtle.forward(altura)
    turtle.left(90)
    turtle.forward(lado)
    turtle.left(90)
    turtle.forward(altura)
    turtle.left(180)
    turtle.forward(altura)
    turtle.right(90)

dibujar_rectangulo(200,100)
turtle.exitonclick()