
def agregaPreferencia (diccionario,persona,preferencia):
    '''dict,str,str -> None
    '''
    if persona in diccionario and preferencia not in diccionario[persona]:
        diccionario[persona].append(preferencia)
    elif persona not in diccionario:
        diccionario[persona] = [preferencia]


    return diccionario

d = {"Ana" : ["Trap","Hockey"],
"Luis": ["Futbol","basket"]}
agregaPreferencia(d,"Luis","mtb")
print(d)

import random
#-------------------------------------------

lista = []
for i in range(200):
    lista.append(random.randint(0,99))

diccionario = {}
lista_ceros = 10*[0]
for i in range(10):
    diccionario[i*10] = lista_ceros[:]
    
for numero in lista:
    posicion_en_dic = (numero // 10) * 10
    posicion_en_lista = numero % 10
    diccionario[posicion_en_dic][posicion_en_lista] += 1

print(diccionario)


#------------------------------------------------------
