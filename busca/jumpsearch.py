import math

lista = [1,2,3,4,5,6,7,8,9,10]
tam = len(lista)
m = int(math.sqrt(tam))
print(m)
valor = 5
i = 0
def jump_search(lista, valor):
    i = 0
    while i <= tam:
        if lista[i] == valor:
            print('achei')
            return 'encontrado'
        else:
            i = i + m

jump_search(lista, valor)
