# JOGO DA VELHA POR UM INICIANTE EM PYTHON

# VARIÁVEIS PRINCIPAIS
tabuleiro = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
jogador_atual = "X"
contador_de_jogadas = 1


# FUNÇÃO MOSTRAR TABULEIRO
# Mostrar tabuleiro de forma clara e visual.
# Idealmente, sem repetição de código, e com separadores ortganizados.
def mostrar_tabuleiro(tab):
    for linha in tab:
        for coluna in linha:
            print(" | ", coluna, end=" ")
        print(" | ")
        print(" | --- + --- + --- | ")


# FUNÇÃO MOSTRAR JOGADOR ATUAL
# Exibe qual jogador fará a jogada atual.
def mostrar_jogador_atual(jogador):
    if jogador == "X":
        print ("JOGADOR X")
    else:
        print ("JOGADOR O")


# FUNÇÃO PARA VALIDAR INTERVALO ENTRADA DO USUARIO
# Verifica se a entrada é um número inteiro entre 1 e 9.
def valida_intervalo_entrada_jogada(input_usuario):
    if input_usuario in range(1, 10):
        return input_usuario
    else:
        print(">> NÚMERO FORA DO INTERVALO <<")
        return False


# FUNÇÃO PARA VERIFICAR SE O NUMERO DIGITADO ESTÁ LIVRE
# Verifica se o número informado pelo jogador ainda existe no tabuleiro (ou seja, se não foi substituido por "X" ou "O")
def posicao_livre(tabuleiro, jogada):
    for linha in tabuleiro:
        for numero in linha:
            if jogada == numero:
                return jogada
    print(">> ESCOLHA OUTRO NUMERO <<")
    return False

# FUNÇÃO PARA ATUALIZAR O TABULEIRO COM A JOGADA ATUAL
# Substituir a posição escolhida pelo jogador pela letra correspondente ("X" ou "O").
def atualiza_tabuleiro(tabuleiro, jogada, jogador):
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == jogada:
                tabuleiro[linha][coluna] = jogador

# FUNÇÃO PARA ATUALIZAR JOGADOR
def atualizar_jogador(jogador):
    return 'O' if jogador == 'X' else 'X'

while contador_de_jogadas <= 9:
    print(f"JOGADA: {contador_de_jogadas}")
    mostrar_tabuleiro(tabuleiro)
    mostrar_jogador_atual(jogador_atual)

    while True:
        try:
            jogada_atual = input("Digite um número de 1 e 9: ")
            jogada_atual = int(jogada_atual)
        except ValueError as error:
            print(">> DIGITE UM VALOR VÁLIDO <<")
            continue # PARA REPETIR O LOOP NA NOVA TENTATIVA
        
        jogada_atual = valida_intervalo_entrada_jogada(jogada_atual)
        if not jogada_atual:
            continue # NÚMERO FORA DO INTERVALO

        jogada_atual = posicao_livre(tabuleiro, jogada_atual)
        if not jogada_atual:
            continue # POSIÇÃO ESTÁ OCUPADA

        break # PARA SAIR DO LOOP INTERNO E ATUALIZAR O TABULEIRO

    atualiza_tabuleiro(tabuleiro, jogada_atual, jogador_atual)
    jogador_atual = atualizar_jogador(jogador_atual)
    contador_de_jogadas += 1 