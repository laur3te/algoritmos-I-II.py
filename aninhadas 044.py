#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto. vista no cartão: 5% de desconto. em até 2x no cartão: preço formal. 3x ou mais no cartão: 20% de juros

print("\x1b[95m-=\x1b[00m"*20)

valor = float(input("Valor do produto: R$"))
pagamento = int(input('''FORMAS DE PAGAMENTO
[ 1 ] À VISTA DINHEIRO/CHEQUE
[ 2 ] À VISTA CARTÃO
[ 3 ] 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO
Opção: '''))

print("\x1b[95m=-\x1b[00m"*20)

if pagamento == 1:
    desconto = valor - (valor * 0.10)
    print(f"\nELEGÍVEL A \x1b[32m10 PORCENTO\x1b[00m DE DESCONTO\nVALOR FINAL: R${desconto}")

elif pagamento == 2:
    desconto = valor - (valor * 0.05)
    print(f"ELEGÍVEL A \x1b[34m5 PORCENTO\x1b[00m DE DESCONTO\nVALOR FINAL: R${desconto}")

elif pagamento == 3:
    print(f"NÃO ELEGÍVEL A PROMOÇÕES.\nVALOR: R${valor}")

elif pagamento == 4:
    vezes = int(input("Em quantas vezes deseja parcelar? "))
    valor_final = valor + (valor * 0.20)
    parcela =  valor_final / vezes
    print(f"PARCELAS: {vezes}X de R${parcela:.2f} com JUROS\nO valor final com juros é R${valor_final:.2f}")
else:
    valor = 0
    print("Opção inválida!")
    