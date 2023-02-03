def jugar(intento):
    respuesta = input("De que color es la naranja?")
    if respuesta != "naranja":
        if intento < 3:
            print('\nFallaste, intenta de nuevo')
            intento += 1
            jugar(intento)
        else:
            print('\nPerdiste')
    else:
        print('\nGanaste!')

jugar(1)