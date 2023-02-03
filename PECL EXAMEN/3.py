def es_filaraki(numero):
    '''int -> bool
    OBJ = Verificar si un número es filaraki
    PRE = n > 0
    '''
    anterior_digito = numero % 10
    actual_digito = numero // 10
    
    numero_f = actual_digito**2 + anterior_digito**2
    if numero_f == 1:
        return True
    else:
        for i in range(8):
            anterior_digito = numero_f % 10
            actual_digito = numero_f // 10
            numero_f = actual_digito**2 + anterior_digito**2
            if numero_f == numero:
                return False

#iNTENTAR CON UN WHILE                

print(es_filaraki(11))
