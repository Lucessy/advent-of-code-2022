import random
frase = ['perro','niño','nube','padre','es','esta','come','mira','ama','el','la','al','en']

for i in range(5):
    longitud_aleatoria = random.randint(3,10)
    for j in range(longitud_aleatoria):
        print(random.choice(frase),"", end="")
    print()

