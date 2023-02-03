def NumeroEnBinario(num):
    '''int -> str'''
    if num == 0:
        binario = ''
    else:
        binario = NumeroEnBinario(num//2) + str(num % 2)
    return binario

print(NumeroEnBinario(5))