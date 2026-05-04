class Players:
    def __init__(self):
        self.max = 10 # limite fixo de 10 jogadores
        self.players = [None] * self.max
        self.head = -1
        self.tail = -1

    def getPhysicalIndex(self, node):
        return (self.head + node) % self.max

    def isEmpty(self):
        return self.head == -1
    
    def isFull(self):
        return (self.tail + 1) % self.max == self.head
    
    def clearPlayers(self):
        self.players = [None] * self.max
        self.head = -1
        self.tail = -1

    def getNumberOfPlayers(self):
        if self.isEmpty():
            return 0
        if self.tail < self.head:
            return self.max - self.head + self.tail + 1
        return self.tail - self.head + 1

    def printPlayers(self):
        if self.isEmpty():
            print("[ ]")
            return
        
        print("[ ", end="")
        for i in range(self.getNumberOfPlayers()):
            print(f"{self.players[self.getPhysicalIndex(i)]}", end="")
            if i < self.getNumberOfPlayers() - 1:
                print(", ", end="")
            else:
                print(" ", end="")
        print("]")
    
    def searchByIndex(self, node):
        if self.isEmpty() or node < 0 or node >= self.getNumberOfPlayers():
            return None
        return self.players[self.getPhysicalIndex(node)]
    
    def searchByName(self, name):
        if self.isEmpty():
            return -1

        for i in range(self.getNumberOfPlayers()):
            if self.players[self.getPhysicalIndex(i)] == name:
                return i

        return -1
    
    def insertPlayer(self, node, name):
        if self.isFull() or node < 0 or node > self.getNumberOfPlayers():
            return False

        if self.isEmpty():
            self.head = 0
            self.tail = 0
            self.players[0] = name
            return True

        # inserir no início
        if node == 0:
            self.head = (self.head - 1) % self.max
            self.players[self.head] = name
            return True

        # inserir no fim
        if node == self.getNumberOfPlayers():
            self.tail = (self.tail + 1) % self.max
            self.players[self.tail] = name
            return True

        # inserir no meio
        n = self.getNumberOfPlayers()
        if node <= n // 2:
            # deslocar para a esquerda
            self.head = (self.head - 1) % self.max
            i = self.head
            for _ in range(node):
                nxt = (i + 1) % self.max
                self.players[i] = self.players[nxt]
                i = nxt
            self.players[i] = name
        else:
            # deslocar para a direita
            self.tail = (self.tail + 1) % self.max
            i = self.tail
            for _ in range(n - node):
                prev = (i - 1) % self.max
                self.players[i] = self.players[prev]
                i = prev
            self.players[i] = name

        return True

    def insertPlayerAfter(self, name, name2):
        node = self.searchByName(name)
        if node == -1:
            return False
        else:
            self.insertPlayer(node + 1, name2)

    def removePlayer(self, node):
        if self.isEmpty() or node < 0 or node >= self.getNumberOfPlayers():
            return False

        if self.getNumberOfPlayers() == 1:
            self.players[self.getPhysicalIndex(node)] = None
            self.head = -1
            self.tail = -1
            return True

        if node <= (self.getNumberOfPlayers() - 1) // 2:
            # deslocar elementos da esquerda para a direita
            i = self.getPhysicalIndex(node)
            while i != self.head:
                prev = (i - 1) % self.max
                self.players[i] = self.players[prev]
                i = prev
            self.players[self.head] = None
            self.head = (self.head + 1) % self.max
        else:
            # deslocar elementos da direita para a esquerda
            i = self.getPhysicalIndex(node)
            while i != self.tail:
                nxt = (i + 1) % self.max
                self.players[i] = self.players[nxt]
                i = nxt
            self.players[self.tail] = None
            self.tail = (self.tail - 1) % self.max

        return True