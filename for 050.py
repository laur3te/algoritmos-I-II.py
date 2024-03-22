#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

cont = 0
soma = 0
for numeros in range (0, 6):
    num = int(input("Insira um valor: "))
    if num % 2 == 0:
        cont += 1
        soma += num
print(f"Há {cont} números pares e a soma deles é {soma}.")