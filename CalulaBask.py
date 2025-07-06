import math
nome_usuario = input('Olá, como você se chama?')
print('Óla,', nome_usuario, 'seja bem vindo ao CalculaBask')
num_A = float(input('Digite aqui o A da sua equação: '))
if num_A == 0:
    print('O valor de A deve ser diferente de Zero.')
else:
    num_B = float(input('Digite aqui o B da sua equação: '))
    num_C = float(input('Digite aqui o C da sua equação: '))
    num_Delta = (num_B ** 2) - 4 * num_A * num_C
    print('O delta da sua equação é:', num_Delta)
    if num_Delta < 0:
        print('Delta não possui resultados reais')
    elif num_Delta == 0:
        print('A solução possui apenas uma solução real')
        num_X1 = (- num_B + num_Delta ** (1/2)) / (2 * num_A)
        num_X2 = (- num_B - num_Delta ** (1/2)) / (2 * num_A)
        print(f'X1 é igual à', int(num_X1), 'e o X2 é igual à', int(num_X2))
    else:
        num_X1 = (- num_B + num_Delta ** (1/2)) / (2 * num_A)
        num_X2 = (- num_B - num_Delta ** (1/2)) / (2 * num_A)
        print(f'X1 é igual à', int(num_X1), 'e o X2 é igual à', int(num_X2))
