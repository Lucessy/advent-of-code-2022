def volumen_gases (moles, temperatura, presion):
    """float , float, float -> float
    OBJ = Calcular el volumen ocupado por un gas dada una temperatura, presión, nº moles y una costante
    PRE = Presión >= 0 , Temperatura >= 0 """
    #   Constante uniuversal de los gases: 0.082 atm L / Kmol
    return (moles * 0.082 * temperatura)/ presion

def volumen_en_CI (moles):
    "float -> float"
    return volumen_gases(moles,273.15,1)

# Probador
print(volumen_gases(10, 273.15, 1))
print(volumen_en_CI(10))

def volumen_gas (moles , temperatura = 273.15 , presion = 1):
    """ float"""
    return (moles * 0.082 * temperatura) / presion

print(volumen_gas(10 , 280 , 1.5))