def TrianguloValido(lista,j,i,validos):
    '''list -> int
    OBJ = Retorna un entero con los triangulos verificados'''
    estado = True
    if j != len(lista):
        if not Suma(lista[j]):
            estado = False
            validos = TrianguloValido(lista,j+1,0,validos)

        else:
            validos += 1
            validos = TrianguloValido(lista,j+1,0,validos)

        
        return validos
    else:
        return validos

def Suma(lista):
    if lista[0] + lista[1] <= lista[2]:
        return False
    elif lista[0] + lista[2] <= lista[1]:
        return False
    elif lista[1] + lista[2] <= lista[0]:
        return False
    else:
        return True

#Probador
mediciones = [[3,2,1],[4,2.5,3.5],[4,2.5,3.5],[4,2.5,3.5]]
print(TrianguloValido(mediciones,0,0,0))


########################################################

lista_entregas = [{1},{1},{2}]

ruta_recomendada = '01-02-00'
provincias=["Álava", "Albacete", "Alicante", "Almería", "Asturias", "Ávila", "Badajoz", "Barcelona", "Burgos", "Cáceres", "Cádiz", "Cantabria", "Castellón", "Ciudad Real", "Córdoba", "Cuenca", "Gerona", "Granada", "Guadalajara", "Guipúzcoa", "Huelva", "Huesca", "Islas Baleares", "Jaén", "La Coruña", "La Rioja", "Las Palmas", "León", "Lérida", "Lugo", "Madrid", "Málaga", "Murcia", "Navarra", "Orense", "Palencia", "Pontevedra", "Salamanca", "Santa Cruz de Tenerife", "Segovia", "Sevilla", "Soria", "Tarragona", "Teruel", "Toledo", "Valencia", "Valladolid", "Vizcaya", "Zamora", "Zaragoza"]

def DiccionarioCodigo(provincias):
    diccionarioPro = {}
    numero = '00'
    i = 1
    j = 0
    for provincia in provincias:
        if i > 9:
            j += 1
            i = 0
            numero = str(j)+str(i)
            diccionarioPro[provincia] = numero
            i += 1
            
        else:
            numero = str(j)+str(i)
            i += 1
            diccionarioPro[provincia] = numero
    return diccionarioPro


def OrdenRutaReco(lista_entregas,provincias):
    '''Diccionario,Str,Diccionario -> Diccionario
    OBJ : Ordenar ascendentemente la lista de entregas según la ruta_recomendada'''
    Provincias = DiccionarioCodigo(provincias)
    long = len(lista_entregas)-1
    for pasada in range (0 , long ) :
        for i in range (0 , long - pasada ) :
            if (lista_entregas[i]['cod_postal'][:2]) > (lista_entregas[i+1]['cod_postal'][:2]):
                (lista_entregas[i]['cod_postal'][:2]),(lista_entregas[i+1]['cod_postal'][:2]) = (lista_entregas[i+1]['cod_postal'][:2]),(lista_entregas[i]['cod_postal'][:2])


def EntregasEspecificas(provincias,lista_entregas,lugar):

    regalos = []
    for key in provincias:
        if provincias[key] == lugar:
            codigo = key
            break
    i = 0
    for elem in lista_entregas:
        if elem['cod_postal'][:2] == codigo:
            regalos.append(lista_entregas[i]['lista_regalos'])
        i += 1
    return regalos

def SoloRegalos(lista_entregas):
    DiccionarioRegalos = {}
    for elem in lista_entregas:
        if elem['cod_postal'][:2] in DiccionarioRegalos:
            DiccionarioRegalos[elem['cod_postal'][:2]] += elem['lista_regalos']
        else:
            DiccionarioRegalos[elem['cod_postal'][:2]] = elem['lista_regalos']
    
    return DiccionarioRegalos


info_autonomias = {'Catalunya': { 'num_ninnos': 1001000, 'provincias': ['08','25','17','43' ]},
 'Madrid': { 'num_ninnos': 643000, 'provincias': ['28'] },
 'Extremadura':{ 'num_ninnos': 260000, 'provincias': ['10','06'] },
 'Euskadi': { 'num_ninnos': 260000, 'provincias': ['48','20','01'] }}

def MenorNumNiños(info_autonomias,SoloRegalos,lista_entregas):
    suma = 0
    DiccionarioRegalos = SoloRegalos(lista_entregas)
    Menor = {}
    for key in info_autonomias:
        comunidad = key
        provincias = info_autonomias[key]['provincias']
        for codigo in provincias:
            suma += len(DiccionarioRegalos[codigo])
        suma = suma/len(provincias)
        Menor.append(suma)
    Menor.sort()
    ListaMenores = Menor[:4]
    return ListaMenores

