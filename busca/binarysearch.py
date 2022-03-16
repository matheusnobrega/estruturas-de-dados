lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 24,25,26,27,28, 29]

def binarysearch(lista, inicio, fim, valor):
    meio = int((inicio + fim)/2)
    print('Meio:{} inicio:{} fim:{} valor:{} lista:{}'.format(meio, inicio,fim, valor, lista[meio]))

    if meio == (inicio or fim) and valor != lista[meio]:
        print('nao encontrado mas num retorna')
        return True

    if valor == lista[meio]:
        print('encontrado mas num retorna')
        return False

    if valor < lista[meio]:
        fim = meio
        binarysearch(lista, inicio, fim, valor)
    else:
        inicio = meio
        binarysearch(lista, inicio, fim, valor)




retu = binarysearch(lista, 0, len(lista), 9)
print(retu)