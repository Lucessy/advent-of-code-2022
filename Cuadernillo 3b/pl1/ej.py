#10 numeros enteros entre 1 y 100, indicar si esta de manera creciente, decreciente o no
import random


creciente = decreciente = True
anterior = random.randint(1,100)
count = 1
while (creciente or decreciente) and count < 10:
        actual = random.randint(1,100)
        if actual > anterior:
            decreciente = False
        elif actual < anterior:
            creciente = False
        else:
            creciente = decreciente = False
        anterior = actual
        count += 1
if creciente: print("La serie es creciente")
elif decreciente: print("La serie es decreciente")
else: print("La serie no lleva ningún orden")




        


