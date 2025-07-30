# Jogo da Velha em Python por um iniciante

# Criando um tabuleiro
tabuleiro = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def mostrar_tabuleiro(tabuleiro):
    for i in tabuleiro:
        for linha in i:
            print(" | ",linha, end=" ")
        print(" | ")

mostrar_tabuleiro(tabuleiro)

jogador_atual = "X"