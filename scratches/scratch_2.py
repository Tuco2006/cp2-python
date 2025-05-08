#txt = input('Digite uma palavra bonita:')

#print(f'O primeiro caracter é {txt[0]}')
#print(f'O último caracter é {txt[-1]}')
##print(f'O tamanho da string é {len(txt)}')
#print(f'Uma forma de pegar fatias da string é: {txt[2:4]}')
#print(f'Uma forma de pegar fatias da string é: {txt[1::2]}')

i = 0
#while i < len(txt):
    #print(txt[i])


txt1 = 'hj-e-uad-yhn'
txt2 = 'oetmal-epto'
txt = ''

while i < len(txt1) and i < len(txt2):

    print(txt1[i])
    print(txt2[i])
    i += 1
    #if i <= len(txt2):
        #print(txt1[-1])
if len(txt1 + txt2) % 2 == 1:
    txt = txt + txt1[i]
    print(txt)





