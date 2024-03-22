#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior.
# O segundo valor é maior.
# Não existe valor maior, os dois são iguais.

num1 = float(input("Insira o 1° valor: "))
num2 = float(input("Insira o 2° valor: "))

if num1 > num2:
    print(f"O \x1b[92mPRIMEIRO\x1b[00m valor é maior que o segundo.")
elif num1 < num2: 
    print(f"O \x1b[94mSEGUNDO\x1b[00m valor é maior que o primeiro.")
else:
    print(f"O \x1b[94mPRIMEIRO\x1b[00m e o \x1b[93mSEGUNDO\x1b[00m valor são iguais.")