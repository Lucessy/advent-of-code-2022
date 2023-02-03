import math
def distancia_puntos (x , y , z , a , b , c): 
    return math.sqrt((x-a)**2 + (y-b)**2 + (z-c)**2)

def distancia_puntos2(punto1, punto2):
    vector = (punto1[0] - punto2[0], punto1[1] - punto2[1], punto1[2] - punto2[2])
    modulo = math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
    return modulo
    
# Probador
print(distancia_puntos2((1,1,1),(1,0,1)))
print(distancia_puntos(1,1,1,1,0,1))
