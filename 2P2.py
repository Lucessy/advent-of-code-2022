def get_lines():
    '''OBJ = Recoje los datos de un texto y los convierte a una lista'''
    
    lines = open("ejemplo2.txt","r").readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
    return lines

def oponente_lista():
    '''OBJ= Separa la columna 1 en una lista y la columna dos en otra lista respectivamente
    '''
    Oponente = []
    lista = get_lines()
    for i in range(len(lista)):
        Oponente += lista[i][0:1]
    return Oponente

def jugador_lista():
    '''OBJ= Separa la columna 1 en una lista y la columna dos en otra lista respectivamente
    '''
    Jugador = []
    lista = get_lines()
    for i in range(len(lista)):
        Jugador += lista[i][2:3]
    return Jugador


def puntuacion():
    pun_forma = {"A":1,"B":2,"C":3}
    jugador_valores = {"X":"Perder","Y":"Empate","Z":"Ganar"}
    gana_contra = {"A":"C","B":"A","C":"B"}
    pierde_contra = {"C":"A","A":"B","B":"C"}
    gana = 6
    empate = 3

    pierde = puntuaje = 0

    oponente = oponente_lista()
    jugador = jugador_lista()

    longitud = len(jugador)

    j = 0
    for i in jugador:
        jugador[j] = jugador_valores[i]
        j += 1
        
    for j in range(longitud):

        if jugador[j] == "Perder":

            figura = gana_contra[oponente[j]]
            puntuaje += pierde + pun_forma[figura]

        elif jugador[j] == "Empate":

            puntuaje += empate + pun_forma[oponente[j]]

        elif jugador[j] == "Ganar":

            figura = pierde_contra[oponente[j]]

            puntuaje += gana + pun_forma[figura]

    return puntuaje

print(puntuacion())