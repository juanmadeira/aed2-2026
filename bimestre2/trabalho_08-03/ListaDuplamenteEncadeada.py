from No import No


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.ini: No = None
        self.fim: No = None

    # Pronto
    def inserir_no_inicio(self, valor):  # Pronto
        novo_nodo = No(valor)
        if self.is_vazia():
            self.ini = novo_nodo
            self.fim = novo_nodo
            return
        novo_nodo.proximo = self.ini
        self.ini.anterior = novo_nodo
        self.ini = novo_nodo

    # Pronto
    def inserir_no_fim(self, valor):
        if self.is_vazia():
            self.inserir_no_inicio(valor)
            return
        novo_nodo = No(valor)
        self.__inserir_no_fim_recursivo_aux(self.ini, novo_nodo)

    def __inserir_no_fim_recursivo_aux(self, no_atual: No, novo_no: No):
        if no_atual.proximo is None:
            no_atual.proximo = novo_no
            novo_no.anterior = no_atual
            self.fim = novo_no
            return
        self.__inserir_no_fim_recursivo_aux(no_atual.proximo, novo_no)

    # Pronto
    def inserir_no_meio(self, valor, indice):
        if indice <= 0 or self.is_vazia():
            self.inserir_no_inicio(valor)
            return
        if indice > self.get_tamanho():
            self.inserir_no_fim(valor)
            return

        self.__inserir_no_meio_recursivo_aux(self.ini, 0, indice, valor)

    def __inserir_no_meio_recursivo_aux(self, no_atual, indice_atual, indice_alvo, valor):
        if no_atual is None:
            self.inserir_no_fim(valor)
            return
        if indice_atual == indice_alvo:
            novo_nodo = No(valor)
            novo_nodo.anterior = no_atual.anterior
            if novo_nodo.anterior is None:
                self.ini = novo_nodo
            else:
                no_atual.anterior.proximo = novo_nodo
            novo_nodo.proximo = no_atual
            no_atual.anterior = novo_nodo
            return
        self.__inserir_no_meio_recursivo_aux(
            no_atual.proximo, indice_atual + 1, indice_alvo, valor)

    # Pronto
    def exibir_lista(self):
        if self.is_vazia():
            print("Você olha para o nada.")
            return
        valores_da_lista = []
        no_atual = self.ini
        while no_atual != None:
            valores_da_lista.append(str(no_atual.dado))
            no_atual = no_atual.proximo
        return " <-> ".join(valores_da_lista)

    # Pronto
    def remover_todos(self, valor):
        if self.is_vazia():
            print("O nada olha para você.")
            return
        self.__remover_recursivo_aux(self.ini, valor)

    def __remover_recursivo_aux(self, no_atual, valor):
        if no_atual is None:
            return
        proximo = no_atual.proximo
        if no_atual.dado == valor:
            anterior = no_atual.anterior
            if anterior is not None:
                anterior.proximo = proximo
            else:
                self.ini = proximo

            if proximo is not None:
                proximo.anterior = anterior
            else:
                self.fim = anterior
        self.__remover_recursivo_aux(proximo, valor)

    # Pronto
    def ordenar(self):
        if self.get_tamanho() < 2:
            print("Para ordenar essa lista (ou qualquer outra), é necessário que haja ao menos dois elementos nela.")
            return
        self.__insercao_recursiva(self.ini)

    def __insercao_recursiva(self, no_atual):
        if no_atual is None:
            return

        proximo_no = no_atual.proximo

        if no_atual.anterior is not None:
            self.__inserir_ordenado_recursivo(no_atual.anterior, no_atual)
        self.__insercao_recursiva(proximo_no)

    def __inserir_ordenado_recursivo(self, no_lista, novo_no):
        if novo_no is None:
            return
        if no_lista is None:
            return
        if novo_no.dado < no_lista.dado:
            aux = novo_no.proximo
            novo_no.proximo = no_lista
            novo_no.anterior = no_lista.anterior

            no_lista.proximo = aux
            no_lista.anterior = novo_no

            if novo_no.anterior is None:
                self.ini = novo_no
            else:
                novo_no.anterior.proximo = novo_no

            if no_lista.proximo is None:
                self.fim = no_lista
            else:
                no_lista.proximo.anterior = no_lista

            self.__inserir_ordenado_recursivo(novo_no.anterior, novo_no)
        return

    # Pronto
    def is_vazia(self):
        return self.ini is None and self.fim is None

    # Pronto
    def get_tamanho(self):
        contador = 0
        no_atual = self.ini
        while no_atual != None:
            contador += 1
            no_atual = no_atual.proximo
        return contador
