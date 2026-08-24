from Nodo import Nodo

class ArvoreBinaria:
    def __init__(self, valor_raiz=None):
        if valor_raiz is not None:
            self.raiz = Nodo(valor_raiz)
        else:
            self.raiz = None

    def localiza(self, valor, nodo_atual=None):
        if nodo_atual is None:
            nodo_atual = self.raiz

        if nodo_atual is None:
            return None

        if nodo_atual.info == valor:
            return nodo_atual

        # busca recursiva na subárvore esquerda
        res = self.localiza(valor, nodo_atual.esq) if nodo_atual.esq else None
        if res is not None:
            return res

        # busca recursiva na subárvore direita
        return self.localiza(valor, nodo_atual.dir) if nodo_atual.dir else None

    def localizaPai(self, valor, nodo_atual=None):
        if nodo_atual is None:
            nodo_atual = self.raiz

        if nodo_atual is None or self.raiz.info == valor:
            return None

        if (nodo_atual.esq and nodo_atual.esq.info == valor) or \
           (nodo_atual.dir and nodo_atual.dir.info == valor):
            return nodo_atual

        # busca na subárvore esquerda
        if nodo_atual.esq:
            pai = self.localizaPai(valor, nodo_atual.esq)
            if pai:
                return pai

        # busca na subárvore direita
        if nodo_atual.dir:
            pai = self.localizaPai(valor, nodo_atual.dir)
            if pai:
                return pai

        return None

    def insesq(self, pai, filho):
        nodoPai = self.localiza(pai)
        if nodoPai is not None and nodoPai.esq is None:
            nodoPai.esq = Nodo(filho)
            return True
        return False

    def insdir(self, pai, filho):
        nodoPai = self.localiza(pai)
        if nodoPai is not None and nodoPai.dir is None:
            nodoPai.dir = Nodo(filho)
            return True
        return False

    def remfolha(self, valor):
        if self.raiz and self.raiz.info == valor and self.raiz.folha():
            self.raiz = None
            return True

        nodoPai = self.localizaPai(valor)
        if nodoPai:
            if nodoPai.esq and nodoPai.esq.info == valor and nodoPai.esq.folha():
                nodoPai.esq = None
                return True
            if nodoPai.dir and nodoPai.dir.info == valor and nodoPai.dir.folha():
                nodoPai.dir = None
                return True
        return False

    def pre_fixado_esquerda(self, nodo=None, em_inicio=True):
        if em_inicio: nodo = self.raiz
        if nodo is not None:
            print(nodo.info, end=" ")
            self.pre_fixado_esquerda(nodo.esq, False)
            self.pre_fixado_esquerda(nodo.dir, False)
            if em_inicio: print()

    def central_esquerda(self, nodo=None, em_inicio=True):
        if em_inicio: nodo = self.raiz
        if nodo is not None:
            self.central_esquerda(nodo.esq, False)
            print(nodo.info, end=" ")
            self.central_esquerda(nodo.dir, False)
            if em_inicio: print()

    def pos_fixado_esquerda(self, nodo=None, em_inicio=True):
        if em_inicio: nodo = self.raiz
        if nodo is not None:
            self.pos_fixado_esquerda(nodo.esq, False)
            self.pos_fixado_esquerda(nodo.dir, False)
            print(nodo.info, end=" ")
            if em_inicio: print()

    def pre_fixado_direita(self, nodo=None, em_inicio=True):
        if em_inicio: nodo = self.raiz
        if nodo is not None:
            print(nodo.info, end=" ")
            self.pre_fixado_direita(nodo.dir, False)
            self.pre_fixado_direita(nodo.esq, False)
            if em_inicio: print()

    def central_direita(self, nodo=None, em_inicio=True):
        if em_inicio: nodo = self.raiz
        if nodo is not None:
            self.central_direita(nodo.dir, False)
            print(nodo.info, end=" ")
            self.central_direita(nodo.esq, False)
            if em_inicio: print()

    def pos_fixado_direita(self, nodo=None, em_inicio=True):
        if em_inicio: nodo = self.raiz
        if nodo is not None:
            self.pos_fixado_direita(nodo.dir, False)
            self.pos_fixado_direita(nodo.esq, False)
            print(nodo.info, end=" ")
            if em_inicio: print()
