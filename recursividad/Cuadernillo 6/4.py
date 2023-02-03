def TerminoFibonacci(n):
    if n <= 1:
        termino = n
    else:
        termino = TerminoFibonacci(n-1) + TerminoFibonacci(n-2)
    return termino

print(TerminoFibonacci(1))
print(TerminoFibonacci(6))
print(TerminoFibonacci(8))