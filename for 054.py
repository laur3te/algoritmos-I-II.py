#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

contador = 0
from datetime import date

for ano in range(0, 7): #Importa o ano atual, substraí com o ano inserido e verifica se a pessoa tem mais de 21 anos. Itinera sete vezes.
    ano_nascimento = int(input("> "))
    if (date.today().year - ano_nascimento) >= 21: 
        contador += 1 #Contabiliza toda vez que o resultado se encaixar na condição.

print("\x1b[95m=-\x1b[00m"*15) #95 = lilás na tabela ANSI. 
print(f"{contador} atingiram a maior idade.\n{7 - contador} NÃO atingiram a maior idade.")
