lista = [6,2,5,4,9, 1, 7, 3, 8]
flag = 1
while flag == 1:
    flag = 0
    for i in range(len(lista)-1):
        if lista[i+1] != None:
            if lista[i] > lista[i+1]:
                flag = 1
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux


print(lista)

