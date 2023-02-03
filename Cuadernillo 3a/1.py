def importe (importe , pago):
    try:
        importe = float(importe)
        
    except:
        print("El importe en inválido")
        
    if importe >= 100:
        if pago == 1:
            importe_final = importe * 0.95
        elif pago ==2:
            importe_final = importe * 0.98
        else:
            print("Tipo de pago incorrecto")
        return importe_final

    else:
        print(f"Su importe final es: {importe}")


#Probador
#x=input("Introduzca el importe:")
#y=input("Si paga al contado insertar '1' , Si paga con tarjeta insertar '2':")
x = 150.2
y = 1
print(importe(x,y))