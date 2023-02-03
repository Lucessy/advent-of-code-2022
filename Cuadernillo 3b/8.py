def centrarRotulo (rotulo, subrayado, tam_ventana):
 """string, string, int--> None
 OBJ: centra rótulo, subrayado con signos =, +línea encima y debajo
 """
 tam=len(rotulo)
 lado=((tam_ventana-tam)//2)-1 
 print()
 print(' '*lado,rotulo)
 print(' '*lado , subrayado*tam , end='\n')

 


def tabla_multiplicar (n,tam_ventana,simbolo="="):
    long = len("Tabla de multiplicar")
    tam = ((tam_ventana -long)//2)-1
    print(" "*tam,"Tabla de multiplicar")
    print(" "*tam,long*simbolo)

    for i in range(1,n+1):
        print("\t", i,end="")
    print()
    
    for i in range(1,n+1):
        if i < 10:
            print("",i,"|",end="")
        else:
            print(i,"|",end="")
        for j in range(1,n+1):
            if j < 10:
                print("\t",i*j,end="")
            else:
                print("\t",i*j,end="")
        print()


#Probador
tabla_multiplicar(10,70)