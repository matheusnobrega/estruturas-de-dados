class No:

    def __init__(self, valor):
        self.valor = valor
        self.no_esq = None
        self.no_dir = None


class ArvoreBinaria:

    def __init__(self):
        self.raiz = None

    def insere_raiz(self, valor):
        no = No(valor)
        self.raiz = no
        #print(self.raiz.valor)
        #print("passei por aqui")

    def insere_arvore(self, valor):
        if self.raiz == None:
            self.insere_raiz(valor)
        else:
            atual = self.raiz
            anterior = None

            while atual != None:
                anterior = atual
                if atual.valor == valor:
                    return False

                if valor > atual.valor:
                    atual = atual.no_dir
                else:
                    atual = atual.no_esq

            if valor > anterior.valor:
                anterior.no_dir = No(valor)
                print("no direito")
                print(anterior.no_dir.valor)
            else:
                anterior.no_esq = No(valor)
                print("no esquerdo")
                print(anterior.no_esq.valor)

    def busca_arvore(self, valor):
        if self.raiz == None:
            return "arvore esta vazia"

        atual = self.raiz

        while atual != None:
        #    print(atual.valor)
            if atual.valor == valor:
                return "achado o valor"

            if valor > atual.valor:
                atual = atual.no_dir
            else:
                atual = atual.no_esq

        return "Item nao esta inserido na arvore"

def main():
    arvore = ArvoreBinaria()

    arvore.insere_arvore(20)
    arvore.insere_arvore(21)
    arvore.insere_arvore(22)
    arvore.insere_arvore(23)
    arvore.insere_arvore(17)
    arvore.insere_arvore(18)

    x = arvore.busca_arvore(7)
    print(x)


main()