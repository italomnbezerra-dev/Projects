linha = int(input('Qual a quantidade de linhas que deseja? '))
coluna = int(input('Qual a quantidade de colunas que deseja? '))
matrizprincipal = [[0 for _ in range(coluna)] for _ in range(linha)]


def dissecando_matrizes():  # formação da matriz
    for l in range(coluna):
        for c in range(linha):
            matrizprincipal[l][c] = int(
                input(f'Digite o valor da posição [{l},{c}]: '))


def mprincipal():  # matriz principal
    print('\nMatriz principal:')
    for l in range(coluna):
        for c in range(linha):
            print(f' {matrizprincipal[l][c]} ', end=' ')
        print()


def matdiagonal():
    print('\nDiagonal principal:')
    for l in range(coluna):
        for c in range(linha):
            if l == c:
                print(matrizprincipal[l][c], end=' ')
            else:
                print(' ', end=' ')
        print()


def suptriangulo():
    print('\nTriângulo superior:')
    for l in range(linha):
        for c in range(coluna):
            if c >= l:
                print(matrizprincipal[l][c], end=' ')
            else:
                print(' ', end=' ')
        print()


def inftriangulo():
    print('\nTriângulo inferior:')
    for l in range(linha):
        for c in range(coluna):
            if c <= l:
                print(matrizprincipal[l][c], end=' ')
            else:
                print(' ', end=' ')
        print()


# Inicio
dissecando_matrizes()
while True:
    print()
    print('===================')
    print('MENU DE OPÇÕES:')
    print('===================')
    print()
    print('[1] Mostrar a Matriz')
    print('[2] Mostrar a Diagonal Principal')
    print('[3] Mostrar o Triângulo Superior')
    print('[4] Mostrar o Triângulo Inferior')
    print('[5] Sair')
    print()
    print('===================')
    print('OPÇÂO:')
    print('===================')
    print()
    resp1 = int(input(f'Digite aqui sua opção: '))

    if resp1 == 1:
        mprincipal()
    elif resp1 == 2:
        matdiagonal()
    elif resp1 == 3:
        suptriangulo()
    elif resp1 == 4:
        inftriangulo()
    elif resp1 == 5:
        print('O programa foi finalizado')
        break
    else:
        print('Opção inválida, digite novamente uma opção válida.')
