# Leandro Shindi Ekamoto
# Classe para armazenar estados em forma de Arvore
#
class Node(object):

    pai = []
    estado = []
    minimax = 0
    jogador = ""
    filhos = []

pai = Node()

filho_1 = Node()
filho_1.minimax = 1

filho_2 = Node()
filho_2.minimax = 2

pai.filhos.append(filho_1)
pai.filhos.append(filho_2)

print pai.filhos[0].minimax
print pai.filhos[1].minimax
