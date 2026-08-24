from Nodo import Nodo
from ArvoreBinaria import ArvoreBinaria

if __name__ == "__main__":
    arvore = ArvoreBinaria('A')

    #       A
    #      / \
    #     B   C
    #    / \   \
    #   D   E   F
    arvore.insesq('A', 'B')
    arvore.insdir('A', 'C')

    arvore.insesq('B', 'D')
    arvore.insdir('B', 'E')

    arvore.insdir('C', 'F')

    print("Pré-fixado à Esquerda:  ", end="")
    arvore.pre_fixado_esquerda()

    print("Central à Esquerda:     ", end="")
    arvore.central_esquerda()

    print("Pós-fixado à Esquerda:   ", end="")
    arvore.pos_fixado_esquerda()

    print("Pré-fixado à Direita:   ", end="")
    arvore.pre_fixado_direita()

    print("Central à Direita:      ", end="")
    arvore.central_direita()

    print("Pós-fixado à Direita:    ", end="")
    arvore.pos_fixado_direita()

    nodo_e = arvore.localiza('E')
    print(f"\nEndereço localizado para nó 'E': {nodo_e}")
    if nodo_e:
        print(f"O nó 'E' é folha? {nodo_e.folha()}")  # tem de ser True

    nodo_b = arvore.localiza('B')
    if nodo_b:
        print(f"O nó 'B' é folha? {nodo_b.folha()}")  # tem de ser False (tem filhos D e E)

    pai_of_e = arvore.localizaPai('E')
    print(f"Pai do nó 'E': {pai_of_e.info if pai_of_e else 'Nenhum'}")

    pai_of_a = arvore.localizaPai('A')
    print(f"Pai do nó 'A' (Raiz): {pai_of_a.info if pai_of_a else 'Nenhum'}")

    print("\nTentando remover 'B' (não é folha):", arvore.remfolha('B'))  # False
    print("Tentando remover 'E' (é folha):    ", arvore.remfolha('E'))  # True

    print("\nÁrvore após remover a folha 'E' (Central à Esquerda):")
    arvore.central_esquerda()
