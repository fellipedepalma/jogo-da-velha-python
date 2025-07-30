# JOGO DA VELHA EM PYTHON POR UM INICIANTE

# CRIANDO UM TABULEIRO E JOGADOR ATUAL
tabuleiro = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
jogador_atual = "X"
jogadas_feitas = 0

# MOSTRANDO O TABULEIRO 
def mostrar_tabuleiro(tabuleiro):
    for i in tabuleiro:
        for linha in i:
            print(" | ",linha, end=" ") 
        print(" | ")
        print(" | --- + --- + --- | ")

# JOGADORES
def mostrar_jogador_atual(jogador_atual):
    if jogador_atual == "X":
        print("JOGADOR X")
    else:
        print("JOGADOR O")

# VALIDANDO A ENTRADA DA JOGADA
def valida_entrada_jogada(jogada):
    if jogada in range(1, 10):
        return jogada
    else:
        print("JOGADA INVÁLIDA")
        return False

# VERIFICANDO SE POSIÇÃO ESTÁ OCUPADA
def posicao_livre(tabuleiro, jogada):
    for linha in tabuleiro:
        if jogada == linha:
            return True
    return False

# ATUALIZANDO O TABULEIRO
def atualiza_tabuleiro(tabuleiro, jogada_atual, jogador_atual):
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == jogada_atual:
                tabuleiro[linha][coluna] = jogador_atual

# JOGANDO
while jogadas_feitas < 9:
    print("=======================================")
    print(f"JOGO DA VELHA - JOGADA ATUAL:  {jogadas_feitas + 1}")
    print("=======================================")

    mostrar_jogador_atual(jogador_atual)

    mostrar_tabuleiro(tabuleiro)
    
    jogada_atual = valida_entrada_jogada(int(input("Digite um número de 1 a 9 correspondente ao tabuleiro: ")))
    print(jogada_atual)

    esta_livre = posicao_livre(tabuleiro, jogada_atual)

    print(esta_livre)

    if esta_livre:
        atualiza_tabuleiro(tabuleiro, jogada_atual, jogador_atual)

        jogador_atual = 'O' if jogador_atual == 'X' else 'X'
        jogadas_feitas += 1
    else:
        print("FAÇA UMA JOGA VÁLIDA!")