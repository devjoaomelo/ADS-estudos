#Começo da variável volumeFeijoada

def volumeFeijoada():
    while True:
        try:
            volumeF = int(input('Quantos ml de feijoada gostaria?(aceitamos entre 300ml e 5000ml)\n>> '))
            if (volumeF >= 300) and (volumeF <= 5000):
                return volumeF * 0.08#cálculo do valor por volume
            else:
                print('Não trabalhamos com essa quantidade, tente novamente...')
                continue
        except ValueError:
            print('Esse não é um valor numérico inteiro. tente novamente...')
            continue
#Fim da variável volumeFeijoada

#Inicio da variável opcaoFeijoada
def opcaoFeijoada():
    while True:
        print('Menu Opção Feijoada')#menu abaixo detalhado
        opcaoF = input("Escolha o serviço desejado:\nb - Básica  (Feijão + paiol + costelinha)\np - Premium (Feijão + paiol + costelinha + partes de porco) \ns - Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon)\n>>")
        if opcaoF == "b":#multiplicadores por opção
            return 1
        elif opcaoF == "p":
            return 1.25
        elif opcaoF == "s":
            return 1.50
        else:
            print('Não existe esse serviço, tente novamente')
            continue
#Fim da variável opcaoFeijoada

#Inicio da variável acFeijoada
def acFeijoada():
    ac = 0#Acumulador
    while True:
        try:
            acF = int(input('Deseja algum acompanhamento?: \n0 - Não, Encerrar o pedido \n1 - 200g de arroz \n2 - 150g de farofa especial\n3 - 100g de couve cozida\n4-  1 laranja descascada\n>> '))
            if acF == 0:
                return ac
            elif acF == 1:
                ac += 5
            elif acF == 2:
                ac += 6
            elif acF == 3:
                ac += 7
            elif acF == 4:
                ac += 3
            elif acF != (1, 2, 3, 4):#Tratamento de opção errada
                print('Esta não é uma opção válida, tente novamente...')
                continue
            res = input('Deseja mais algum acompanhamento? (s/n) :')
            if res == 's':
                continue
            elif res == 'n':
                return ac #retornado o valor ao sair
        except:#tratamento de except
            print('Você não digitou um comando inválido, tente novamente...')
            continue
#fim da variável acFeijoada

#Programa principal
print('Bem vindo ao programa de feijoada do João Melo! RU: 4195804')
volumeF = volumeFeijoada()
opcaoF = opcaoFeijoada()
acF = acFeijoada()
print(f'o valor a ser pago é: R${((opcaoF * volumeF) + acF)}')#cálculo do valor