def PalabraInvertida(palabra):
    if len(palabra) == 1:
        invertida = palabra
    else:
        invertida = palabra[-1] + PalabraInvertida(palabra[:-1])
    return invertida

print(PalabraInvertida('amor'))
print(PalabraInvertida('hola'))
