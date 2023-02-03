def fuerza (aceleracion , masa):
    """ float, float -> float
    OBJ: Calcular la fuerza dependiendo de su masa y aceleración
    PRE: masa >= 0"""
    return  aceleracion * masa

#   Probador
aceleracion = float(input('Aceleración:'))
masa = float(input('Masa:'))
print(f'Con la aceleración: {aceleracion} y la masa: {masa}. El valor de la fuerza es de: {fuerza(aceleracion, masa)}')

