def CuentaDigitos(num):
    if num//10 == 0: #num < 10
        digitos = 1
    else:
        digitos = 1 + CuentaDigitos(num//10)
    return digitos

print(CuentaDigitos(665749))
print(CuentaDigitos(30000))