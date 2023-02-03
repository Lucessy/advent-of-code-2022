import turtle
def dibujar_triangulo_equilatero(lado , color):
    """float -> None
    OBJ: Dibuja un triangulo equilatero en pantalla a partir del punto de origen
    """
    turtle.color(color)
    turtle.pendown()
    turtle.forward(lado)
    turtle.left(120)
    turtle.forward(lado)
    turtle.left(120)
    turtle.forward(lado)
    turtle.left(120)


dibujar_triangulo_equilatero(100 , "black")