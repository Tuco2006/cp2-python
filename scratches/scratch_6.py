print('Programa verificador se o número é primo')

i = 'Sim'

while i == 'Sim':
    num1 = float(input('Digite o número a ser veriicado:'))
    while num1 != 0:
      num3 = num1 - 1
      div = (num1 % num1)
      div2 = (num1 % 1)
      div3 = num1 % num3
      if div3 != 0 and div == 0 and div2 == 0:
            print('Esse número é primo!')
            i = input('Deseja testar novamente?')
            if i != 'Sim':
                print('Fim do teste')
                break

      else:
          print('Esse número não é primo!')
          i = input('Deseja testar novamente?')
          if i != 'Sim':
              print('Fim do teste')
              break

      if num1 == 0:
          print('Não aceitamos número zero!')
          i = input('Deseja testar novamente?')
          if i != 'Sim':
              print('Fim do teste')
              break




