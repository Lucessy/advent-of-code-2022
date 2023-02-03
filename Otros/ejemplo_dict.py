#EJEMPLO DICCIONARIOS
dicc = {'2':3,4:2.5}

for key,values in dicc.items():
    print(key,values)

lista1 = [1,2,3]
lista2 = lista1[:]

for i in range(5):
    for j in range(5):
        if i==1 and j==1:
            print('SUINT')
            break
    if i==3:
        print('SUUU')
        break

