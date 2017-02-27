import sys

linha, coluna = 5, 5;
matrix = [[0 for x in range(coluna)] for y in range(linha)]




def init(matrix):

    for linha in range(0, 5):
        l = ""
        for coluna in range(0, 5):
            matrix[linha][coluna] = "."

    for x in range(0, 5):
        matrix[0][x] = "-"

    for x in range(0, 5):
        matrix[4][x] = "-"

    for x in range(1, 4):
        matrix[x][0] = "|"

    for x in range(1, 4):
        matrix[x][4] = "|"

def mostra_por_linhas(matrix):
    for linha in matrix:
        l = ""
        for coluna in linha:
            l += str(coluna);
        print l


init(matrix)
mostra_por_linhas(matrix)
