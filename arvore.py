class No:

    def __init__(self, valor):
        self.valor = valor
        self.no_esq = None
        self.no_dir = None


class ArvoreBinaria:

    def __init__(self):
        self.raiz = None
        self.quantidade = None

    def insere_raiz(self, valor):
        no = No(valor)
        self.raiz = no
        self.quantidade += 1


