class Pilha:
    def __init__(self, tamanho):
        self.vetor = [None] * tamanho
        self.lim = tamanho - 1
        self.base = 0
        self.topo = self.base - 1

    def Empilha(self,dado):
        if(self.topo < self.lim):
            self.topo += 1
            self.vetor[self.topo] = dado

    def Excluir(self):
        if self.topo < self.base:
            return None
        dado = self.vetor[self.topo]
        self.vetor[self.topo] = None
        self.topo -= 1
        return dado
    
    def Consulta(self):
        if self.topo >= self.base:
            return self.vetor[self.topo]

    def Destruir(self):
        while self.topo >= self.base:            
            self.Excluir()