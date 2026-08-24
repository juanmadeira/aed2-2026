class Nodo:
    def __init__(self, info):
        self.info = info
        self.esq = None
        self.dir = None

    def folha(self):
        return self.esq is None and self.dir is None
