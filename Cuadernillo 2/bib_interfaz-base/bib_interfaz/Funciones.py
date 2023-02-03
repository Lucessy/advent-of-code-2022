def centrarRotulo (rotulo, subrayado, tam_ventana):
 """string, string, int--> None
 OBJ: centra rótulo, subrayado con signos cualesquiera, +línea encima y debajo
 """
 tam=len(rotulo)
 lado=((tam_ventana-tam)//2)-1 
 print()
 print(' '*lado,rotulo)
 print(' '*lado , subrayado*tam , end='\n')

 