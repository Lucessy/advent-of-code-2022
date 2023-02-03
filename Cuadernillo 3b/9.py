def num_a_romano (num):
    """int -> str
    OBJ = Convertir un número entero a romano del 1 hasta el 2000
    PRE = num > 0"""
    uno =   "I"
    cinco = "V"
    diez =  "X"
    cincuenta = "L"
    cien = "C"
    quinientos = "D"
    mil = "M"
    if 1 <= num <= 2000:
        while num >= 1000:
            print(mil,end="")
            num -= 1000
        
        while num >= 500:
            print(quinientos,end="")
            num -= 500

        while num >= 100:
            print(cien,end="")
            num -= 100
        
        while num >= 50:
            print(cincuenta,end="")
            num -= 50
        
        while num >= 10:
            print(diez,end="")
            num-=10
        
        if num == 9:
            print("IX")
            num -= 9
        
        while 9 > num >= 5:
            print(cinco,end="")
            num -= 5
            print(uno*num)
        

    return num
        
        

        

#Probador
num_a_romano(99)
            
