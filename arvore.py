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
        print(self.raiz.valor)
        print("passei por aqui")

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

                if atual.valor > valor:
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

    def imprime(self):
        atual = self.raiz

        while atual != None:
            print(atual.no_dir)
            print(atual.no_esq)
            atual = atual.no_dir

def main():
    arvore = ArvoreBinaria()

    arvore.insere_arvore(5)
    arvore.insere_arvore(20)
    arvore.insere_arvore(21)


main()