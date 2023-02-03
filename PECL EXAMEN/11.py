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
