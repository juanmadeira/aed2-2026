from arvore import Nodo

#         10
#      /      \
#     5       15
#    / \     /
#   3   8   12

raiz = Nodo(10)
raiz.insesq(10, 5)
raiz.insdir(10, 15)
raiz.insesq(5, 3)
raiz.insdir(5, 8)
raiz.insesq(15, 12)

# raiz.contaNos()
raiz.removeUmFilho(15)
