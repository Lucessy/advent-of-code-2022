def function_pep484 (a: int ,b: int ) -> bool:
    #El símbolo "->" significa lo que tiene que retornar
    """Args:
            a: The first parameter
            b: The second parameter

        Returns:
            True if a > b, Flase otherwise.
     """
    return a >= b
#Probador
#print(function_pep484(2, 3))


def area_triangulo (a,b,c):
    """ float , float , float -> float
        OBJ: Calcular el área del un triangulo a partir de las longitudes de su lado
        PRE: a,b,c >= 0 """



def square (x: float): pass
""" Con la sentencia: <pass> se puede postergar el uso de una función siendo su salida <None> """
# Test code
print(square (5))


def ejemplo ():
    import time
    print('Fecha :', time.strftime ("%x"))
    print('Hora :', time.strftime (" %H : %M : %S " ))

ejemplo()

# Es una definición que da como retorno una magnitud o un valor por asi decirlo. Por ejemplo:

def hipotenusa (a,b):
    """ float, float -> float
    OBJ: Calculasr hipotenusa triangulo rectangulo, catetos: a,b
    PRE: a,b > 0 """
    

# En esta otra nos da un procedimiento el cual imprime,ordena o solo nos muestra algo, 
# no se espera de ellos un valor como retorno (Como en la función):

def saludar (nombre):
    """ Str -> None 
    OBJ : Función para saludar a alguien
    """
    print (f'Hola, {nombre}!')

#Probador
saludar("María")

#   Si queremos utilizar alguna variable global, su uso correcto 
#   es ajustar la función para que sea simple y especifica teniendo una entrada
#   y una salida que retorne un valor.

def media_aritmetica (x,y):
    """  int , int -> float
    OBJ: Media aritmetica de dos valores enteros
    """
    media = ( x + y ) / 2 
    return media

#   Con esta función ahora podemos insertarle valores como mejor veamos, asi también
#   nos retornará el valor dado

a = int(input('Insertar número entero:'))
b = int(input('Insertar número entero:'))
print(f'La media aritmetica de {a} y {b} es: {media_aritmetica(a,b)}')
