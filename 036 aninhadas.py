# Exercício 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.


print("\x1b[95m", "=-"*20, "\x1b[00m")

valor_casa = float(input("Valor da casa: "))
salario = float(input("Salário do comprador: "))
anos = int(input("Em quantos anos irá pagar: "))

print("\x1b[95m =-\x1b[00m"*20)

prestacao = valor_casa / (12 * anos) #A mensalidade é calculada por meses, então devemos transformar anos em meses.
sal_30 = salario * 0.30 #30% do salário do comprador

if prestacao >= sal_30: #Se a prestação for maior que 30% do salário do cliente, o empréstimo será negado.
    print("Empréstimo \x1b[31mNEGADO\x1b[00m!")
else: 
    print("Empréstimo \x1b[32mAPROVADO\x1b[00m!")
