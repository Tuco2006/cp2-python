produto1 = float(0.5)
produto2 = float(1.0)
produto3 = float(3.5)
produto4 = float(8.0)


print('Seja bem vindo à loja de Brinquedos DaniloGay, temos os seguintes brinquedos: Homem Aranha, Homem de Ferro, Super-Man e Mulher Maravilha!')
qual = input('Qual produto o senhor deseja comprar? Pressione "0" para finalizar a compra!')
valor = 0
while qual != 0:
    if qual == 'Homem Aranha':
        valor += produto1
        qual = input(f'Valor R${valor}. Próximo produto:')

    elif qual == 'Homem de Ferro':
        valor += produto2
        qual = input(f'Valor R${valor}. Próximo produto:')

    elif qual == 'Super-Man':
        valor += produto3
        qual = input(f'Valor R${valor}. Próximo produto:')

    elif qual == 'Mulher Maravilha':
        valor += produto4
        qual = input(f'Valor R${valor}. Próximo produto:')

    if qual == '0':
        print(f'Seu pedido ficou no valor de R${valor}')
        break





