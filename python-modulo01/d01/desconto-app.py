"""Elabore um programa em Python que:
⦁	Entre com o valor unitário do produto (Lembrar que número decimal é feito com ponto e não vírgula);
⦁	Entre com a quantidade desse produto;
⦁	O programa deve retornar o valor total sem desconto;
⦁	O programa deve retornar o valor total após o desconto;
⦁	Deve-se utilizar estruturas if, elif e else (EXIGÊNCIA 1 de 1);"""

def entrada():
    while True:
        try:
            valor_prod = float(input('Digite o valor do produto: '))
            quantidade_prod = int(input('Quantidade do produto: '))
            if valor_prod < 0 or quantidade_prod < 0:
                print('Não trabalhamos com números negativos, tente novamente...')
                continue
            total_p = desconto_prod(valor_prod, quantidade_prod)
            total = (f'{valor_prod*quantidade_prod:.2f}').replace('.',',')
            print(f'O valor total do produto sem desconto foi de R${total}')
            print(f'{total_p}')
        except ValueError:
            print('Você não digitou um valor válido, tente novamente...')
            continue
     
def desconto_prod(valor, qtd):
    if 1 >= qtd <= 4:
        desconto = ('Não há desconto para essa quantidade')
        return desconto
    elif 5 >= qtd <= 19:
        desconto =(f'O valor com desconto 3% foi: R${qtd * (valor * 0.97):.2f}').replace(".",",") #3% de desconto caso a quantidade for superior e 5 e menor que 20
        return desconto
    elif 20 >= qtd <= 99:
        desconto = (f'O valor com desconto de 6% foi: R${qtd * (valor * 0.94):.2f}').replace(".",",") #6% de desconto caso a quantidade for superior a 20 e menor que 99
        return desconto
    elif 100 >= qtd:
        desconto = (f'O valor com desconto de 10% foi: R${qtd * (valor * 0.90):.2f}').replace(".",",") #10% de desconto caso a quantidade for superior a 100
        return desconto
        

# Programa principal
entrada()
desconto_prod()

