# Possuem disciplina restrita de acesso:
# - somente o primeiro nó (top)

# Restrições as operações:
# - inserção
# - remoção
# - consulta

# Comportamento:
# - Last In, First Out (LIFO)
#   o último elemento inserido é o primeiro a ser retirado

class Stack:
    def __init__(self, size):
        self.size = size
        self.items = [None] * self.size
        self.limit = self.size - 1
        self.bottom = 0
        self.top = self.bottom - 1

    def is_empty(self):
        if self.top == -1:
            return True
        return False

    def push(self, data):
        if(self.top < self.limit):
            self.top += 1
            self.items[self.top] = data

    def pop(self):
        if self.top < self.bottom:
            return None
        data = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return data
    
    def show(self):
        return self.items
    
    def last_item(self):
        if self.top >= self.bottom:
            return self.items[self.top]
        
    def destroy(self):
        while self.top >= self.bottom:            
            self.pop()

    def upside_down(self):
        if not self.is_empty():
            aux = Stack(self.size)
            while self.top >= self.bottom:
                aux.push(self.last_item())
                self.pop()

            self.items = aux.items
            del(aux)
        
pilha = Stack(10)
pilha.push("a")
pilha.push("b")
pilha.push("c")
print(pilha.show())
pilha.upside_down()
print(pilha.show())