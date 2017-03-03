#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Leandro Shindi Ekamoto
# Jogo da Velha Utilizando MiniMax
#

from Node import Node

linha, coluna = 5, 5;

# Nó raiz
raiz = Node()
estado_atual = Node()
estado_atual.estado = [[0 for x in range(coluna)] for y in range(linha)]

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

	pontuacaoMaquina = 0

    #for x in coluna:
    #    if (estado[0][x] != null and estado[0][x] == estado[2][x] and estado[0][x] == estado[4][x]):
    #        if (estado[0][x] == "X"):
    #            pontuacaoMaquina = 1
    #        else:
    #            pontuacaoMaquina = -1

    #return None


# function ehTerminal(estado,encerra) {	// verifica se estado é terminal, retornando seu valor de utilidade
# 	var x,y;							// retorna null caso não seja estado terminal
# 	var brancos = 0;					// encerra = 0 para calcular o valor de utilidade durante a geração da árvore
# 	var utilidade = null;				//         = 1 para encerrar o jogo quando estado for terminal

# 	for (y=0; y<3; y++)		// testa linhas
# 		if (estado[y][0] != undefined && estado[y][0] == estado[y][1] && estado[y][0] == estado[y][2]) {
# 			utilidade = (estado[y][0] == "X")? 1: -1;	// utilidade 1 para X (CPU), -1 para O (humano)
# 			break;
# 		}
# 	if (!utilidade)			// testa colunas
# 		for (x=0; x<3; x++)
# 			if (estado[0][x] != undefined && estado[0][x] == estado[1][x] && estado[0][x] == estado[2][x]) {
# 				utilidade = (estado[0][x] == "X")? 1: -1;
# 				break;
# 			}
# 	if (!utilidade)			// testa diagonais
# 		if ( estado[1][1] != undefined && (
# 			 (estado[0][0] == estado[1][1] && estado[0][0] == estado[2][2]) ||
# 			 (estado[0][2] == estado[1][1] && estado[0][2] == estado[2][0])    ) )
# 			utilidade = (estado[1][1] == "X")? 1: -1;

# 	for (y=0; y<3; y++)
# 		for (x=0; x<3; x++)
# 			if (estado[y][x] == undefined)	// conta espaços em branco no tabuleiro
# 				brancos++;

# 	if (utilidade)					// se achou um vencedor
# 		if (encerra)
# 			if (utilidade > 0)		// utilidade > 0 venceu CPU
# 				termina("Eu ganhei!");
# 			else
# 				termina("Você ganhou!");	// essa mensagem nunca será exibida :)
# 		else
# 			return utilidade*(brancos+1); 	// retorna valor de utilidade - nº de casas vagas dá um peso maior,
# 											// favorecendo a escolha da jogada vitoriosa no nível mais raso
# 	else
# 		if (!brancos)				// se não tem mais espaços em branco também é terminal...
# 			if (encerra)
# 				termina("Empatamos!");
# 			else
# 				return 0;			// ...com utilidade 0 (empate)
# 		else
# 			return null; 			// se ainda tem brancos, não é terminal
# }


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

                nd.filhos.append(novo_no)

                # Essa recursividade não funciona...
                #Filhos somente se não for terminal
                #if(novo_no.minimax != None):
                #    gera_filhos(novo_no)

# Computador joga
def joga_computador():

    global estado_atual
    print "Joga Computador"

    maximo = -1

    for filho in estado_atual.filhos:
        if(filho.minimax != None and filho.minimax > maximo):
            maximo = filho.minimax
            estado_atual = filho

    # Verifica se atingiu estado terminal, encerrando o jogo
    eh_terminal(estado_atual.estado, 1);
    print "Fim Joga Computador"

# Laço infinito para pegar jogada
while(jogar):
    posicao = raw_input("Escolha uma posição para jogar. 0 para sair: ")

    set_posicao(posicao)
    mostra_por_linhas(estado_atual.estado)

    if(len(raiz.filhos) == 0):
        # Usuário joga primeiro
        # TODO criar rotina para poder setar inicio e jogada
        # do computador
        raiz.jogador = "0"
        raiz.estado = estado_atual.estado

        gera_filhos(raiz)
        print "*****************************"
        # Listando filhos inseridos
        contador = 0
        for nd in raiz.filhos:
            print "----------------------------"
            mostra_por_linhas(nd.estado)
            contador = contador+1
            if(contador==10):
                break
        print "----------------------------"

        #print "*****************************"

    joga_computador()

    mostra_por_linhas(estado_atual.estado)

    # Listando filhos inseridos
    #for nd in estado_atual.filhos:
    #    print "----------------------------"
    #    mostra_por_linhas(nd.estado)
    #print "*****************************"
    #print "----------------------------"
