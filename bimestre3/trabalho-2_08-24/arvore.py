class Nodo:
    def __init__(self, info):
        self.info = info
        self.esq = None
        self.dir = None
        self.qtdNos = 0

    def insesq(self, pai, filho):
        nodoPai = self.localiza(pai)
        if (nodoPai != None and nodoPai.esq == None):
            nodoPai.esq = Nodo(filho)
        
    def insdir(self, pai, filho):
        nodoPai = self.localiza(pai)
        if (nodoPai != None and nodoPai.dir == None):
            nodoPai.dir = Nodo(filho)    

    def folha(self):
        return (self.esq == None and self.dir == None)

    def remfolha(self, valor):
        nodoPai = self.localizaPai(valor)
        if (nodoPai):
            if (nodoPai.esq and nodoPai.esq.info == valor and nodoPai.esq.folha()):
                nodoPai.esq = None
            if (nodoPai.dir and nodoPai.dir.info == valor and nodoPai.dir.folha()):
                nodoPai.dir = None
     
    def localiza(self, valor):
        end = None
        if self.info == valor:
            end = self
        if end == None and self.esq != None:
            end = self.esq.localiza(valor)
        if end == None and self.dir != None:
            end = self.dir.localiza(valor) 
        return end
        
    def localizaPai(self, valor):            
        if self.esq and self.esq.info == valor:
            return self
        if self.dir and self.dir.info == valor:
            return self
        if self.esq:
            aux = self.esq.localizaPai(valor)
            if aux:
                return aux
        if self.dir:
            aux = self.dir.localizaPai(valor) 
            if aux:
                return aux
        return None      
    
    def prefixesq(self):
        print(self.info)
        if self.esq:
            self.esq.prefixesq()
        if self.dir:
            self.dir.prefixesq()
    
    def prefixdir(self):
        print(self.info)
        if self.dir:
            self.dir.prefixdir()
        if self.esq:
            self.esq.prefixdir()

    # def contaNos(self):
    #     self.qtdNos += 1
    #     if self.dir:
    #         self.dir.contaNos()
    #     if self.esq:
    #         self.esq.contaNos()
    #     print(self.qtdNos)

    def removeUmFilho(self, valor):
        if self.localiza(valor).esq and self.localiza(valor).dir:
            return False

        if self.localiza(valor).esq:
            filho = self.localiza(valor).esq.info
            self.localiza(valor).esq = None
        if self.localiza(valor).dir:
            filho = self.localiza(valor).dir.info
            self.localiza(valor).dir = None

        self.localiza(valor).info = filho

    # def espelha(self):
    #     if self.esq:
    #         if self.dir:
    #             self.esq.info = self.dir.info
    #         else:
    #             self.esq.info = None
    #     if self.dir:
    #         if self.esq:
    #             self.dir.info = self.esq.info
    #         else:
    #             self.dir.info = None
