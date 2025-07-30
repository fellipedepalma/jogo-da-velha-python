# Jogo da Velha em Python por um iniciante

# Criando um tabuleiro
tabuleiro = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def mostrar_tabuleiro(tabuleiro):
    for i in tabuleiro:
        for linha in i:
            print(" | ",linha, end=" ")
        print(" | ")

jogador_atual = "X"

# VALIDANDO A JOGADA
def validando_jogada(jogada):
    if jogada in range(1, 10):
        return True
    else:
        print("Jogada inválida")

mostrar_tabuleiro(tabuleiro)

# Jogando

validando_jogada(jogada = int(input("Digite um número de 1 a 9 correspondente ao tabuleiro: ")))
