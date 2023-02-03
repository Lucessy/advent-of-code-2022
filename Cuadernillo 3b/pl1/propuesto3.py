def dibujar_rectangulo (ancho,alto,simbolo):
    for i in range(alto):
        for j in range(ancho):
            print(simbolo,end="")
        print()

dibujar_rectangulo(5,3,"#")
