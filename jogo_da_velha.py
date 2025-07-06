linha = 3
coluna = 3
matrizprincipal = [['-' for _ in range(coluna)] for _ in range(linha)]
jogadores = ['X', 'O']
jogada = 0


def mostrar_tabuleiro():
    print('\nTABULEIRO DE JOGO DA VELHA:')
    print('---------------')
    for l in range(linha):
        for c in range(coluna):
            print(f'| {matrizprincipal[l][c]} ', end='')
        print('|')
    print('---------------')


def posicao_para_indices(pos):
    pos -= 1
    return pos // 3, pos % 3


def checar_vitoria(simbolo):
    # Checa linhas, colunas e diagonais
    for i in range(3):
        if all(matrizprincipal[i][j] == simbolo for j in range(3)):
            return True
        if all(matrizprincipal[j][i] == simbolo for j in range(3)):
            return True
    if all(matrizprincipal[i][i] == simbolo for i in range(3)):
        return True
    if all(matrizprincipal[i][2-i] == simbolo for i in range(3)):
        return True
    return False


def tabuleiro():
    jogada = 0
    while True:
        mostrar_tabuleiro()
        jogador = jogadores[jogada % 2]
        try:
            pos = int(input(f'Jogador {jogador}, escolha uma posição (1-9): '))
        except ValueError:
            print('Digite um número válido!')
            continue
        if pos < 1 or pos > 9:
            print('Posição inválida!')
            continue
        l, c = posicao_para_indices(pos)
        if matrizprincipal[l][c] != '-':
            print('Posição já ocupada!')
            continue
        matrizprincipal[l][c] = jogador
        if checar_vitoria(jogador):
            mostrar_tabuleiro()
            print(f'Jogador {jogador} venceu!')
            break
        jogada += 1
        if jogada == 9:
            mostrar_tabuleiro()
            print('Empate!')
            break


tabuleiro()
