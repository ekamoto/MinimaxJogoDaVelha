#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Leandro Shindi Ekamoto
# Jogo da Velha Utilizando MiniMax
#

from Node import Node

# Nó raiz
raiz = Node()

linha, coluna = 5, 5;

matrix = [[0 for x in range(coluna)] for y in range(linha)]

# Lista de Estados
class ListaEstados(list):

    def push(self, item):
        self.append(item)

lista_estados = ListaEstados([])

jogar = 1

def monta_matrix(matrix):

    matrix[0][1] = "|"
    matrix[0][3] = "|"

    for x in range(0, 5):
        matrix[1][x] = "-"

    matrix[2][1] = "|"
    matrix[2][3] = "|"

    for x in range(0, 5):
        matrix[3][x] = "-"

    matrix[4][1] = "|"
    matrix[4][3] = "|"

    indice = 1
    for linha in range(0, 5):
        for coluna in range(0, 5):
            if(matrix[linha][coluna] !="|" and matrix[linha][coluna]!="-"):
                matrix[linha][coluna] = indice
                indice = indice + 1

def mostra_por_linhas(matrix):
    for linha in matrix:
        l = ""
        for coluna in linha:
            l += str(coluna);
        print "  "+l

monta_matrix(matrix)
mostra_por_linhas(matrix)

# Set posições
def set_posicao_1():
    matrix[0][0] = "0"
    return "Set Posição 1\n"

def set_posicao_2():
    matrix[0][2] = "0"
    return "Set Posição 2\n"

def set_posicao_3():
    matrix[0][4] = "0"
    return "Set Posição 3\n"

def set_posicao_4():
    matrix[2][0] = "0"
    return "Set Posição 4\n"

def set_posicao_5():
    matrix[2][2] = "0"
    return "Set Posição 5\n"

def set_posicao_6():
    matrix[2][4] = "0"
    return "Set Posição 6\n"

def set_posicao_7():
    matrix[4][0] = "0"
    return "Set Posição 7\n"

def set_posicao_8():
    matrix[4][2] = "0"
    return "Set Posição 8\n"

def set_posicao_9():
    matrix[4][4] = "0"
    return "Set Posição 9\n"

# Get posições
def get_posicao_1():
    return matrix[0][0]

def get_posicao_2():
    return matrix[0][2]

def get_posicao_3():
    return matrix[0][4]

def get_posicao_4():
    return matrix[2][0]

def get_posicao_5():
    return matrix[2][2]

def get_posicao_6():
    return matrix[2][4]

def get_posicao_7():
    return matrix[4][0]

def get_posicao_8():
    return matrix[4][2]

def get_posicao_9():
    return matrix[4][4]

def set_sair():
    global jogar
    jogar = 0
    return "Set sair\n"

def set_posicao(posicao):

    switcher = {
        "0": set_sair,
        "1": set_posicao_1,
        "2": set_posicao_2,
        "3": set_posicao_3,
        "4": set_posicao_4,
        "5": set_posicao_5,
        "6": set_posicao_6,
        "7": set_posicao_7,
        "8": set_posicao_8,
        "9": set_posicao_9
    }

    func = switcher.get(posicao, lambda: "Posição Inválida")

    return func()

def copia_matrix(matrix):
    novo = [[0 for x in range(5)] for y in range(5)]
    for linha in range(0, 5):
        for coluna in range(0, 5):
            novo[linha][coluna] = matrix[linha][coluna]
    return novo

def eh_terminal(estado, encerra):

    # TODO: Diego
    return None

def gera_filhos(nd):

    # lista_estados = ListaEstados([])

    jogador = "X" if nd.jogador == "0" else "0"

    for linha in range(0, 5):
        for coluna in range(0, 5):
            if(nd.estado[linha][coluna] != "|" and nd.estado[linha][coluna] != "-" and nd.estado[linha][coluna] != "0" and nd.estado[linha][coluna] != "X"):

                novo_estado = copia_matrix(nd.estado)
                novo_estado[linha][coluna] = jogador

                novo_no = Node()
                novo_no.pai = nd
                novo_no.jogador = jogador
                novo_no.minimax = eh_terminal(novo_estado, 0)
                novo_no.estado = novo_estado

                # Filhos somente se não for terminal
                if(novo_no.minimax != None):
                    gera_filhos(novo_no)

                nd.filhos.append(novo_no)

                #lista_estados.push(novo_estado);


# Laço infinito para pegar jogada
while(jogar):
    posicao = raw_input("Escolha uma posição para jogar. 0 para sair: ")

    set_posicao(posicao)

    # Usuário joga primeiro
    # TODO criar rotina para poder setar inicio e jogada
    # do computador
    raiz.jogador = "0"
    raiz.estado = matrix

    gera_filhos(raiz)

    print "*****************************"
    # mostra_por_linhas(matrix)
    # Listando filhos inseridos
    for nd in raiz.filhos:
        print "----------------------------"
        mostra_por_linhas(nd.estado)
    print "----------------------------"

    print "*****************************"



    #mostra_por_linhas(matrix)
