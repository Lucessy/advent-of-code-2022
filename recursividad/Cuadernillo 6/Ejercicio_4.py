
def fibonacci(n):
    """ int -> int
    OBJ: Da el termino n de la sucesión de fibonacci.
    PRE: n >= 0 """
    if n <= 1:
        fib = n
    else:
        fib = fibonacci(n-1) + fibonacci(n-2)
    return fib

# Probador
print(f'La serie de fibonacci(5) es: {fibonacci(5)}')
