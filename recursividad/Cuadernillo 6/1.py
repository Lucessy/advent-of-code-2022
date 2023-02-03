def EstaEnLista(lista,elem):
    '''List, float -> bool'''
    if len(lista) == 0:
        estaEnLista = False  
    elif elem == lista[0]:
        estaEnLista = True
    else:
        estaEnLista = EstaEnLista(lista[1:],elem)
    return estaEnLista

#Probador
Lista = [1,0,0,0,2,19.5]
print(EstaEnLista(Lista,19.5))