import math
qname = input('Olá, como você se chama?')
print('Óla,', qname, 'seja bem vindo ao CalculaBask')
numA = float(input('Digite aqui o A da sua equação: '))
if numA == 0:
    print('O valor de A deve ser diferente de Zero.')
else:
    numB = float(input('Digite aqui o B da sua equação: '))
    numC = float(input('Digite aqui o C da sua equação: '))
    numDelta = (numB ** 2) - 4 * numA * numC
    print('O delta da sua equação é:', numDelta)
    if numDelta < 0:
        print('Delta não possui resultados reais')
    elif numDelta == 0:
        print('A solução possui apenas uma solução real')
        numX1 = (- numB + numDelta ** (1/2)) / (2 * numA)
        numX2 = (- numB - numDelta ** (1/2)) / (2 * numA)
        print(f'X1 é igual à', int(numX1), 'e o X2 é igual à', int(numX2))
    else:
        numX1 = (- numB + numDelta ** (1/2)) / (2 * numA)
        numX2 = (- numB - numDelta ** (1/2)) / (2 * numA)
        print(f'X1 é igual à', int(numX1), 'e o X2 é igual à', int(numX2))
