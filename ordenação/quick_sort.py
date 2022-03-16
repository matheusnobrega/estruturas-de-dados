lista = [3, 1, 0, 5, 18, 32, 2,44, 4]

def quick_sort(lista, pivo):
    menor = []
    maior = []
    for item in lista:
        if item > pivo:
            maior.append(item)
        else:
            menor.append(item)

    print(maior)
    print(menor)

quick_sort(lista, 18)
