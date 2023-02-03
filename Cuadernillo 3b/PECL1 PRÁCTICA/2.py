import math
def nice_fourth (num):
    """int -> bool
    OBJ = Verifica si un número es nice fourth
    PRE = num > 0
    """
    raiz_cuarta_num = (num ** (1/4))
    return raiz_cuarta_num == int(raiz_cuarta_num)
        

num_prueba = 255
if nice_fourth(num_prueba):
    print(f"Es nice fourth: {num_prueba}")
else:
    print(f"No es un nice fourth: {num_prueba}")

def es_nice_fourth_entre_valores (num_min, num_max):
    """int -> bool
    OBJ = Verifica si un número es nice fourth
    PRE = num > 0
    """
    for i in range(num_min,num_max+1):
        if nice_fourth(i): print(i,end=" ")
            
num1 = 10
num2 = 2000
print(f"Para los valores: {num1} y {num2}, son nice fourth:",end="")
es_nice_fourth_entre_valores(num1,num2)