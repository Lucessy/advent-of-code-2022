import random
def SumaPares(num1,num2):
    if num1 == num2:
        if num1%2 == 0:
            suma = num1
        else:
            suma = 0
    else:
        if num1%2 == 0:
            suma = num1 + SumaPares(num1+1,num2)
        else:
            suma = SumaPares(num1+1,num2)

    return suma

print(SumaPares(0,11))