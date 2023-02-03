def formula (a,b,c):
    return (a**3 * (b**2 - 2*a*c))/(2*b)

a = float(input("a ->"))
b = float(input("b ->"))
c = float(input("c ->"))

resultado =  (a**3 * (b**2 - 2*a*c))/(2*b)
print(resultado)
print(formula(a,b,c))