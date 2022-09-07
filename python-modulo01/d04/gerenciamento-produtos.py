
listaProdutos = []#lista
#Inicio da variável cadastrarProduto
def cadastrarProduto(rp):
    print('Bem vindo ao cadastro de produtos')
    print(f'O RP do produto a ser cadastrado é: {rp}')
    nome = input('Digite o nome do produto\n:> ')
    fabricante = input('Digite o fabricante do produto\n:> ')
    valor = float(input('Digite o valor do produto\n:> '))
    dicionarioProduto = {'rp'         : rp, #dicionário para armazenar a lista
                         'nome'       : nome,
                         'fabricante' : fabricante,
                         'valor'      : valor}
    listaProdutos.append(dicionarioProduto.copy())#gerando uma cópia para o listaProdutos
#Fim da variável cadastrarProduto

#Inicio da variável consultarProduto
def consultarProduto():
    while True:
        try:
            print('Bem vindo a Consulta de produtos') #Menu de consulta produtos
            opConsultar = int(input('Digite a opção desejada:\n'
                                    '1- Consultar todos os produtos:\n'
                                    '2- Consultar por RP:\n'
                                    '3- Consultar por Fabricante:\n'
                                    '4- Retornar:'))
            if opConsultar == 1:
                print('Bem vindo ao consultar TODOS')
                for produto in listaProdutos: #silecionar cada dicionario da minha lista
                    for key, value in produto.items():# selecionar cada conjunto chave/valor do dicionario (ex:'nome' : salsicha)
                        print(f'{key} : {value}')
            elif opConsultar == 2:
                print('Bem vindo a consulta por RP(registro do produto)')
                entrada = int(input('Digite o RP desejado: '))
                for produto in listaProdutos:
                    if(produto['rp'] == entrada):
                        for key, value in produto.items():
                            print(f'{key} : {value}')
            elif opConsultar == 3:
                print('Bem vindo a consulta por FABRICANTE')
                entrada = input('Digite o FABRICANTE desejado: ')
                for produto in listaProdutos:
                    if (produto['fabricante'] == entrada):
                        for key, value in produto.items():
                            print(f'{key} : {value}')
            elif opConsultar == 4:
                break
            else:
                print('Essa opção é inválida, tente novamente...')
        except ValueError:
            print('Esse não é um valor válido')
#fim da variável consultarProduto

#Inicio da variável removerProduto
def removerProduto():
    print('Bem vindo a remoção de produtos')
    entrada = int(input('Digite o RP para remoção: '))
    for produto in listaProdutos:
        if (produto['rp'] == entrada):
            listaProdutos.remove(produto)
#fim da variável removerProduto

#Programa principal
print('Bem-vindo ao controle de produtos João Melo. RU: 4195804')
registroproduto = 0 #gerador de códigos para os itens
while True: #menu de opções
    try:
        opcao = int(input('Digite a opção desejada:\n1 - Cadastrar produto\n'
                          '2 - Consultar produto\n'
                          '3 - Remover produtos\n'
                          '4 - Sair\n'
                          '>:'))
        if opcao == 1:
            registroproduto += 1
            cadastrarProduto(registroproduto)#acumulador de rp(código) gerando códigos unicos para os produtos
        elif opcao == 2:
            consultarProduto()
        elif opcao == 3:
            removerProduto()
        elif opcao == 4:
            print('Finalizando programa')
            break
        else:
            print('Essa opção é inválida, tente novamente...')
            continue
    except ValueError:
        print('Não é um valor válido')
        registroproduto -= 1 # tratamento de número de registro caso erre no cadastro
        continue
