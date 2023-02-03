def media_aritmetica (x,y):
    """  int , int -> float
    OBJ: Media aritmetica de dos valores enteros
    """
    media = ( x + y ) / 2 
    return media

#   Probador
import random
a = random.randint(1,100)
b = random.randint(1,100)
mm = media_aritmetica(a,b) + 90
print(mm)

n = 2
n % 2 != 0