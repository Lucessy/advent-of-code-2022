def condiciones_ideales (presion , temperatura):
    """ float , float-> bool"""
    return presion == 1.0 and temperatura == 273.15



#   Probdor
print(condiciones_ideales(1 , 273.15))