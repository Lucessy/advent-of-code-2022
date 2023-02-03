def mililitros_pintas (mililitros):
    """float -> float
    OBJ: Convertir mililitros a pintas.
    PRE: mililitros >= 0"""

    return mililitros / 473.176473

#   Probador
print(mililitros_pintas(800))