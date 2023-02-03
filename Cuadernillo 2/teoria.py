# 2 inputs , 0 outputs      -> a /
def f1 (n1 , n2):
    print(random.randint(n1, n2))


#  2 inputs , 2 outputs     ->  b ->
import random
from subprocess import BELOW_NORMAL_PRIORITY_CLASS           #   ->
def f2 (n1 , n2):
    alea1 = random.randint(n1, n2)
    alea2 = random.randint(n1, n2)
    return alea1, alea2

#Probador                     /  c ->
x, y = f2(0,100)


# 0 inputs , 1 output          / d  /
def f3 ():
    return random.randint(1,6)

# 0 inputs , 0 outputs
def f4 ():
    print(random.randint(1,6))

    #escribe un sub. que determine si un nmro está en sus limites naturales

def esta_en_limites (n, lim_inf , lim_sup):
    """ float , float , float -> booooooool """
    return lim_inf <= n <= lim_sup

print(0 % 3 == 0)