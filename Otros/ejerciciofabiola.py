def calculo_nave_personas ( comb_total , comb_inicio , comb_persona):
    """ int , int, int -> int
    OBJ = Calcular cuantas personas entran en la nave para ir a la Luna.
    PRE = comb_inicio <= comb_total """
# Comb = Combustible
    return (comb_total - comb_inicio) // comb_persona 

# Probador
comb_total = a =  600
comb_inicio = b = 450
comb_persona = c = 200
print(f'Las personas que caben en la nave son: {calculo_nave_personas(a , b, c)}')