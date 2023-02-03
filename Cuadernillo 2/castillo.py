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

#dibujar_cuadrado(200)
#turtle.exitonclick()

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
    
#dibujar_triangulo_equilatero(200)
#turtle.exitonclick()

def dibujar_casa (lado, altura , color_rectangulo="black" , color_triangulo="black"):
    """ float , float , str , str -> None
    OBJ: Dibuja una casa con los lados y la altura dadas"""
    dibujar_rectangulo(lado , altura , color_rectangulo)
    turtle.penup()
    turtle.left(180)
    turtle.forward(altura)
    turtle.right(90)
    dibujar_triangulo_equilatero(lado, color_triangulo)
    turtle.penup()
    turtle.forward(lado)
    turtle.right(90)
    turtle.forward(altura)
    turtle.left(90)
    




def dibujar_castillo (lado_torre, altura_torre, color_rect="black" , color_trian="black"):
    """ float, float, float, float, float , str , str -> None
    OBJ: Dibuja un castillo en el centro de la pantalla"""
    turtle.penup()
    turtle.backward(lado_torre + (lado_torre/2))
    dibujar_casa(lado_torre , altura_torre , color_rect , color_trian )
    dibujar_casa(lado_torre * 2 , altura_torre * 2 , color_rect , color_trian)
    dibujar_casa(lado_torre , altura_torre , color_rect , color_trian)
    


dibujar_castillo(75  , 50 , color_trian="red")
turtle.exitonclick()