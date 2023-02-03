def en_circulo (x , y):
    """ float , float -> bool
    """
    return x**2 + y**2 == 1000


#Probador
print(input('Coordenada x: '))
print(input('Coordenada y: '))
print(en_circulo())