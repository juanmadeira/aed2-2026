class Nodo:
    def __init__(self, dado):
        self.info = dado
        self.prox = None

class Pilha:
    def __init__(self):
        self.topo = None
    
    def Vazia(self):
        return self.topo is None
    
    def Empilhar(self, dado):
        novo = Nodo(dado)
        if(not self.Vazia()):
            novo.prox = self.topo
        self.topo = novo
    
    def Excluir(self):
        if(not self.Vazia()):
            aux = self.topo            
            self.topo = aux.prox 
            del aux

    def Consultar(self):
        if(not self.Vazia()):
            return self.topo.info
    
    def Destruir(self):
        while(not self.Vazia()):
            self.Excluir