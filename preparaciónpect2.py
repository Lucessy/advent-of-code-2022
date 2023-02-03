def suma(v):
    aux = 0
    for elemento in v:
        if elemento[b]:
            aux = aux + elemento[a]
    return aux

#Si necesitamos la posición hacemos un range
#si no for elemento in v

stuff = []
word = 'hola mi nombre es adri'.split()
print(word)
for w in word:
    stuff.append([w.upper(),w.lower(),len(w)])
print(stuff)

def recursividad(x,y):
    if (y == 0 or x == y):
        valor = 1
    else:
        print('x=',x,'y=',y)
        valor = recursividad(x-1,y-1) + recursividad(x-1,y)
    return valor

print(recursividad(5,3))


