lista = [3, 1, 0, 5, 18, 32, 2,44, 4]
tam_lista = len(lista)

for i in range(tam_lista):
    chave = lista[i]
    for j in range(i+1, tam_lista):
        if chave > lista[j]:
            chave = lista[j]
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

print(lista)