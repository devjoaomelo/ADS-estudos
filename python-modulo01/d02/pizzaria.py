ac = 0  # acumulador de valor
at = ''  # acumulador de texto

print('Bem vindo(a) a Pizzaria do João Melo. RU: 4195804')  # identificador
print('-'*27,  'Cardápio',  '-'*26)
print('|  Código  |Descrição   | Pizza Média - M |  Pizza Grande - G |')
print('|    21    |Napolitana  |        R$ 20,00 |           R$ 26,00|')
print('|    22    |Margherita  |        R$ 20,00 |           R$ 26,00|')
print('|    23    |Calabresa   |        R$ 25,00 |           R$ 32,50|')
print('|    24    |Toscana     |        R$ 30,00 |           R$ 39,00|')
print('|    25    |Portuguesa  |        R$ 30,00 |           R$ 39,00|')
print('-'*63)

while True:
    tamanho = str(input('Qual o tamanho da pizza? (M/G)\n>>').upper())
    if tamanho[0] not in 'GM':
        print('Tamanho inválido')
        continue
    codigo = int(input('Qual o código da pizza?'))
    if codigo > 25 or codigo < 21:
        print('Código inválido, tente novamente...')
        continue

    # Tamanho M
    if tamanho[0] == 'M':
        if codigo == 21:
            ac += 20
            at += 'Napolitana média - R$20,00\n'
        elif codigo == 22:
            ac += 20
            at += 'Marguerita média - R$20,00\n'
        elif codigo == 23:
            ac += 25
            at += 'Calabresa média - R$25,00\n'
        elif codigo == 24:
            ac += 30
            at += 'Toscana média - R$30,00\n'
        elif codigo == 25:
            ac += 30
            at += 'Portuguesa média - R$30,00\n'

    # Tamanho G

    if tamanho[0] == 'G':
        if codigo == 21:
            ac += 20
            at += 'Napolitana grande - R$26,00\n'
        elif codigo == 22:
            ac += 20
            at += 'Marguerita grande - R$26,00\n'
        elif codigo == 23:
            ac += 25
            at += 'Calabresa grande - R$32,50\n'
        elif codigo == 24:
            ac += 30
            at += 'Toscana grande - R$39,00\n'
        elif codigo == 25:
            ac += 30
            at += 'Portuguesa grande - R$39,00\n'

    # pergunta para adicionar mais uma pizza ou não

    continuar = str(input('Deseja pedir mais uma pizza? (S/N)\n>>').upper())
    if continuar[0] == 'S':
        continue
    else:
        break

    # resumo do pedido
print(f'Você pediu:\n{at}\no valor total da conta é: R${ac},00')
