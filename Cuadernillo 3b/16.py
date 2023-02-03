import random
frase = ['perro','niño','nube','padre','es','esta','come','mira','ama','el','la','al','en']
intentos = 0
respuesta = "No"

while respuesta != "Si":
    for i in range(1):
        longitud_aleatoria = random.randint(3,10)
        for j in range(longitud_aleatoria):
            print(random.choice(frase),"",end="")
        print()
    respuesta = input("¿La oración tiene sentido? Responda Si o No: ")
    intentos += 1

print(f"Le tomó: {intentos} intento(s) conseguir una oración con sentido :D")
    

