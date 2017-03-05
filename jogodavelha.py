#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Leandro Shindi Ekamoto
# Diego Takaki
#
# Jogo da Velha Utilizando MiniMax
#

from Node import Node


linha, coluna = 5, 5;

# Nó raiz
raiz = Node([],[],None,None,[])
estado_atual = Node([],[],None,None,[])
estado_atual.estado = [[0 for x in range(coluna)] for y in range(linha)]
pilha = []

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

monta_matrix(estado_atual.estado)

# Set posições
def set_posicao_1():
    #matrix[0][0] = "0"
    estado_atual.estado[0][0] = "0"
    return "Set Posição 1\n"

def set_posicao_2():
    #matrix[0][2] = "0"
    estado_atual.estado[0][2] = "0"
    return "Set Posição 2\n"

def set_posicao_3():
    #matrix[0][4] = "0"
    estado_atual.estado[0][4] = "0"
    return "Set Posição 3\n"

def set_posicao_4():
    #matrix[2][0] = "0"
    estado_atual.estado[2][0] = "0"
    return "Set Posição 4\n"

def set_posicao_5():
    #matrix[2][2] = "0"
    estado_atual.estado[2][2] = "0"
    return "Set Posição 5\n"

def set_posicao_6():
    #matrix[2][4] = "0"
    estado_atual.estado[2][4] = "0"
    return "Set Posição 6\n"

def set_posicao_7():
    #matrix[4][0] = "0"
    estado_atual.estado[4][0] = "0"
    return "Set Posição 7\n"

def set_posicao_8():
    #matrix[4][2] = "0"
    estado_atual.estado[4][2] = "0"
    return "Set Posição 8\n"

def set_posicao_9():
    #matrix[4][4] = "0"
    estado_atual.estado[4][4] = "0"
    return "Set Posição 9\n"

# Get posições
def get_posicao_1():
    return estado_atual.estado[0][0]

def get_posicao_2():
    return estado_atual.estado[0][2]

def get_posicao_3():
    return estado_atual.estado[0][4]

def get_posicao_4():
    return estado_atual.estado[2][0]

def get_posicao_5():
    return estado_atual.estado[2][2]

def get_posicao_6():
    return estado_atual.estado[2][4]

def get_posicao_7():
    return estado_atual.estado[4][0]

def get_posicao_8():
    return estado_atual.estado[4][2]

def get_posicao_9():
    return estado_atual.estado[4][4]

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

    # return None
    pontuacaoMaquina = 0
    espacosVazios = 9

    for x in range(0,5):
       if (estado[0][x] is not None and estado[0][x] == estado[2][x] and estado[0][x] == estado[4][x]):
           if (estado[0][x] == "X"):
                # print "ENTREI AQ"
                pontuacaoMaquina = 1
           else:
                # print "ENTREI AQ TBTBTBTBTB"
                pontuacaoMaquina = -1

    if(pontuacaoMaquina == 0):
        for y in range(0,5):
            if(estado[0][x] is not None and estado[y][0] == estado[y][2] and estado[y][0] == estado[y][4]):
                if (estado[y][0] == "X"):
                    # print "AQUI TBTBTB"   
                    pontuacaoMaquina = 1
                else:
                   pontuacaoMaquina = -1

    if(pontuacaoMaquina == 0):
        if(estado[2][2] is not 0 and (estado[0][0] == estado[2][2] and estado[0][0] == estado[4][4]) or (estado[0][5] == estado[2][2] and estado[0][5] == estado[4][0])):
            if (estado[2][2] == "X"):
               pontuacaoMaquina = 1
            else:
               pontuacaoMaquina = -1

    for i in range(0,5):
        for j in range(0,5):
            if (estado[i][j] == "X" or estado[i][j] == "0"):
                espacosVazios -= 1

    if(pontuacaoMaquina != 0):
        if(encerra == 1):
            if(pontuacaoMaquina > 0):
                #termina() utilizar func termina..
                print("Computador wins")
                set_sair()
            else:
                print "Pontuação da Maquina " + str(pontuacaoMaquina) + " Espaços em branco " + str(espacosVazios) + " É pra terminar? " + str(encerra) 
                print("Output impossível")
                set_sair()
        else:
            peso = pontuacaoMaquina * (espacosVazios + 1)
            print "PESO: " + str(peso)
            return peso

    else:
        if(espacosVazios == 0):
            if(encerra == 1):
                print("Todo mundo é bom, empatou")
                set_sair()
            else:
                return None
        else:
            return None

# Calcula MiniMax de cada nó
def calcula_minimax(nodo):

    min = 9999
    max = -1

    # Percorre todos os filhos do nodo
    for filho in nodo.filhos:

        # Se um filho ainda nao tem um valor minimax (nao e folha da arvore)
        if (filho.minimax == None):
            # Chama a funcao recursivamente para aquele filho
            calcula_minimax(filho)

        # Guarda valor max (maior minimax entre os filhos)
        if (max == -1 or filho.minimax > max):
            max = filho.minimax

        # guarda valor min (menor minimax entre os filhos)
        if (min == 9999 or filho.minimax < min):
            min = filho.minimax;

    # Se a proxima jogada e da CPU, retorna valor max
    if (nodo.jogador == "0"):
        nodo.minimax = max
    else:
        # Caso contrario, retorna valor min
        nodo.minimax = min

def gera_filhos(nd):

    # lista_estados = ListaEstados([])
    global pilha

    jogador = "X" if nd.jogador == "0" else "0"

    for linha in range(0, 5):
        for coluna in range(0, 5):
            if(nd.estado[linha][coluna] != "|" and nd.estado[linha][coluna] != "-" and nd.estado[linha][coluna] != "0" and nd.estado[linha][coluna] != "X"):

                novo_estado = copia_matrix(nd.estado)
                novo_estado[linha][coluna] = jogador

                novo_no = Node([],[],None,None,[])
                novo_no.pai = nd
                novo_no.jogador = jogador
                novo_no.minimax = eh_terminal(novo_estado, 0)
                print "AAAAAAAAAAAAAAAAAA MINIMAX " + str(novo_no.minimax)
                novo_no.estado = novo_estado

                pilha.append(novo_no)
                nd.filhos.append(novo_no)

# Computador joga
def joga_computador():

    global estado_atual

    maximo = -1

    for filho in estado_atual.filhos:
        if(filho.minimax != None and filho.minimax > maximo):
            maximo = filho.minimax
            estado_atual = filho

    # Verifica se atingiu estado terminal, encerrando o jogo
    eh_terminal(estado_atual.estado, 1);

# Laço infinito para pegar jogada
while(jogar):

    mostra_por_linhas(estado_atual.estado)

    posicao = raw_input("Escolha uma posição para jogar. 0 para sair: ")

    set_posicao(posicao)

    mostra_por_linhas(estado_atual.estado)

    if(len(raiz.filhos) == 0):

        # Usuário joga primeiro
        # TODO criar rotina para poder setar inicio e jogada
        # do computador
        raiz.jogador = "0"
        raiz.estado = estado_atual.estado

        pilha.append(raiz)

        while(len(pilha) > 0):
            no = pilha.pop(len(pilha)-1)
            gera_filhos(no)

        # Testando os filhos da primeira camada
        if(0):
            print "**************FILHOS DA RAIZ***************"
            # Listando filhos inseridos
            for nd in raiz.filhos:
                print "----------------------------"
                mostra_por_linhas(nd.estado)

            print "*****************************"

        print "Calculando pontos"
        # Calcula todos os pontos de cada nó
        calcula_minimax(raiz)
        print "Fim pontos"

        #print "*****************************"

    print "Joga Computador"
    joga_computador()
    print "Fim Joga Computador"

    print "Estado atual"
    mostra_por_linhas(estado_atual.estado)
    print "Fim Estado atual"

    # Listando filhos inseridos
    #for nd in estado_atual.filhos:
    #    print "----------------------------"
    #    mostra_por_linhas(nd.estado)
    #print "*****************************"
    #print "----------------------------"
