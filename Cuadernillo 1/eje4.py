INGRESO_TOTAL = 24000 #no es una constante? lo pone como una variable
HIJOS_TOTAL = 2
ingreso_imponible = INGRESO_TOTAL - 600 - HIJOS_TOTAL*60
impuesto_pagar = ingreso_imponible / 3 #tmb ingreso_imponible / 3
print(f"Su ingreso total es de: {INGRESO_TOTAL} .Los impuestos que tendrá que pagar son: {impuesto_pagar}")