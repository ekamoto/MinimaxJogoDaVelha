#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Leandro Shindi Ekamoto
# Jogo da Velha Utilizando MiniMax
#

linha, coluna = 5, 5;

matrix = [[0 for x in range(coluna)] for y in range(linha)]

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
    return "Set Posição 1\n"

def set_posicao_2():
    return "Set Posição 2\n"

def set_posicao_3():
    return "Set Posição 3\n"

def set_posicao_4():
    return "Set Posição 4\n"

def set_posicao_5():
    return "Set Posição 5\n"

def set_posicao_6():
    return "Set Posição 6\n"

def set_posicao(posicao):

    switcher = {
        "1": set_posicao_1,
        "2": set_posicao_2,
        "3": set_posicao_3,
        "4": set_posicao_4,
        "5": set_posicao_5,
        "6": set_posicao_6
    }

    func = switcher.get(posicao, lambda: "Posição Inválida")

    return func()


# Laço infinito para pegar jogada
vencedor = 0
while(vencedor!=1):
    posicao = raw_input("Escolha uma posição para jogar: ")

    print set_posicao(posicao)
    mostra_por_linhas(matrix)
