def superficie_regalo (largo,ancho,alto):
    '''int, int, int -> 
    OBJ = Calcula la superficie necesaria para envolver un regalo más un extra que es el área del lado más pequeño.
    PRE = 0 < largo,ancho,alto
    '''
    superficie = 2*(largo*ancho) + 2*(ancho*alto) + 2*(alto*largo)
    if largo < ancho < alto:
        menor = largo
    elif alto < ancho < largo:
        menor = alto
    else:
        menor = ancho
    extra = menor*menor
    print(f"Se necesitan: {superficie+extra} cm2 en total para envolver el regalo, superficie: {superficie} cm2, extra: {extra} cm2")

import random
def es_representativo (minutos, likes,visualizaciones):
    '''int, int, int -> bool
    OBJ = Verifica si unos determinados minutos, likes y visualizaciones son representativos de los contenidos de ElMorenux
    PRE = 0 <= minutos,likes,visualizaciones'''
    visua_det = 1e7
    likes_det = 1e6
    min_det = 8
    return minutos < min_det and likes > likes_det and visualizaciones > visua_det

num_videos = random.randint(1,1000)
num_videos_represen = 0
duracion_media = 0
for i in range(num_videos):
    minutos = random.randint(1,60) 
    likes = random.randint(100,1e10)
    visualizaciones = random.randint(100,1e10)
    if es_representativo(minutos,likes,visualizaciones):
        duracion_media += minutos
        num_videos_represen += 1

print("La duración media de todos los vídeos representativos es de:",duracion_media/num_videos_represen)

def parejas_que_cumplen(altitud,distancia,objetivo,error):
    '''lista(int),lista(int),float,float -> None
    OBJ = Calcular las parejas de altitud-distancia que quedaron más cerca del valor objetivo junto con el margen de error
    PRE = 0 < '''
    suma_max = objetivo + error
    num_pares = 0
    print("La(s) pareja(s) que cumple(n) cuya suma quedó cerca del objetivo:",end="")
    for altitud_1 in altitud:
        for distancia_1 in distancia:
            suma_anterior = altitud_1 + distancia_1
            if objetivo <= suma_anterior <= suma_max:
                pareja = altitud_1,distancia_1
                num_pares += 1
                print(" ",pareja,end="")
    print(end=". ")
    print("Número de pareja(s):",num_pares)

