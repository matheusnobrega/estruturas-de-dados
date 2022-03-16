lista = [6,2,5,4,9,1,7,3,8]
lista_aux = []
for i in range(1, len(lista)):
    j = i - 1
    chave = lista[i]

    while j >= 0 and lista[j] > chave:
        lista[j+1] = lista[j]
        j -= 1

    lista[j+1] = chave

print(lista)