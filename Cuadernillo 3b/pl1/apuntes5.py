#1,2,3,8,19,86,455...

#n = n-1 + n-2**2 + n-3

def serie (n):
    """int -> int
    OBJ = Calcular el número "n" de una serie dada
    PRE =
    """
    n_3=1
    n_2=2
    n_1=3
    if 0 < n <= 3:
        print(n)
    else:
        for i in range(n-3):
            num = n_1 + n_2**2 + n_3
            n_3 = n_2
            n_2 = n_1
            n_1 = num
        print(num)

serie(5)
