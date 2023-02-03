def metro_barn (metro):
    """float -> float
    OBJ: Convertir metros a Barn
    PRE= metro >= 0"""
    return metro / (10**(-28))

def barn_metro (barn):
    """float -> float
    OBJ: Convertir Barn a metro
    PRE= Barn >= 0"""
    return barn * (10**(-28))

#Probador
print(barn_metro(3))
print(metro_barn(10))