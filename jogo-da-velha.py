# Jogo da Velha em Python por um iniciante

# Criando um tabuleiro
tabuleiro = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
jogador_atual = "X"

def mostrar_tabuleiro(tabuleiro):
    for i in tabuleiro:
        for linha in i:
            print(" | ",linha, end=" ")
        print(" | ")

# JOGADORES
def mostrar_jogador_atual(jogador_atual):
    if jogador_atual == "X":
        print("Jogador X")
    else:
        print("Jogador O")

# VALIDANDO A JOGADA
def validando_jogada(jogada):
    if jogada in range(1, 10):
        return True
    else:
        print("Jogada inválida")

# JOGANDO
while True:
    mostrar_tabuleiro(tabuleiro)
    mostrar_jogador_atual(jogador_atual)
    validando_jogada(jogada = int(input("Digite um número de 1 a 9 correspondente ao tabuleiro: ")))
    break