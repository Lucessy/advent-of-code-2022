def Fibonacci (n):
    #Caso básico
    if (n==0) or (n==1):
        parejas = 1
    #Si no, llamamos recursivamente
    else:
        parejas = Fibonacci(n-1) + Fibonacci(n-2)
    return parejas


print(Fibonacci(5))
