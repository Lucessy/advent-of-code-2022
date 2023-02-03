def posicion (A,elem , inicio , fin ):
    """ list , object , int , int -> int
    OBJ : Posicion en una lista entre 2 limites , None si no esta
    Utiliza el algoritmo de busqueda binaria recursiva
    PRE : lista ordenada
    """
    if inicio > fin: pos = None
    else :
        centro = ( inicio + fin ) // 2
        if A[ centro ] == elem : pos = centro
        elif elem < A[ centro ]: pos = posicion (A,elem , inicio , centro -1)
        else : pos = posicion (A,elem , centro +1 , fin )
    return pos


def ascender_menor (v, primero , ultimo ) :
    """ lista , int , int -> None
    OBJ : Encuentra el menor en un rango y lo lleva a la
    primera posicion . Modifica la lista .
    """
    for i in range (ultimo , primero , -1) :
        if (v[i] < v[i -1]) :
            v[i] , v[i -1] = v[i -1] , v[i]

def ordenar_burbuja (v,inicio ,fin ) :
    """ lista , int , int -> None
    OBJ : Ordena ascendentemente una lista entre dos
    posiciones . Metodo burbuja . """
    for pasada in range (inicio ,fin -1) :
        ascender_menor (v, pasada , fin)

def ordenar_burbuja (v) :
    """ lista -> None
    OBJ : Ordena una lista completa ascendentemente .
    Metodo burbuja . Modifica la lista .
    """
    long = len(v) - 1
    # haremos long - 1 pasadas : 10 elementos -> 9 pasadas
    for pasada in range (0 , long ) :
        # en cada pasada comparamos el elemento i con el i+1
        for i in range (0 , long - pasada ) :
        # cambiamos de posicion si el izquierdo es mayor ,
        # para ordenar ascendente
            if (v[i] > v[i +1]) : v[i] , v[i +1] = v[i+1] , v[i]

def ordenar_seleccion (A) :
    """ lista -> None
    OBJ : Ordena ascendentemente una lista .
    Metodo de seleccion . Modifica la lista . """
    for inicio_pasada in range (len (A) ) :
        # Encuentra el menor de la parte desordenada
        posicion_menor = inicio_pasada
        for i in range ( inicio_pasada + 1 , len (A) ) :
            if A[i] < A[ posicion_menor ]:
                posicion_menor = i
    # Intercambia el primero con el menor
    A[ inicio_pasada ] , A[ posicion_menor ] = A[ posicion_menor ] , A[ inicio_pasada ]
