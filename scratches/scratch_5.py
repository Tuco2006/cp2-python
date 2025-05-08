print('Jogo de PAR OU ÍMPAR')

i = 'Sim'

while i == 'Sim':
    num1 = float(input('Digite o primeiro número:'))
    num2 = float(input('Digite o segundo número:'))
    soma = num1 + num2
    if soma % 2 != 0:
        print('A soma dos números é ÍMPAR')
        i = input('Deseja jogar novamente?')
    elif soma % 2 == 0:
        print('A soma é PAR')
        i = input('Deseja jogar novamente?')
    if i != 'Sim':
        print('Fim de jogo!')
        break