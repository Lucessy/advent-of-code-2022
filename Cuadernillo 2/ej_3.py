def TIEA (TNA, m):
    """float, int -> float
    OBJ: Calcular la TIEA en función de la TNA y de los períodos de capitalización
    PRE: TNA >= 0, 0 < m <= 12"""
    return (1 + (TNA/m) )**(m-1)

#   Probador
print(TIEA(12000, 4), 'Interés Efectivo Anual')