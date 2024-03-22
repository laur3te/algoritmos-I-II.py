#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM, Até 14 anos: INFANTIL, Até 19 anos: JÚNIOR,  Até 25 anos: SÊNIOR, Acima de 25 anos: MASTER

from datetime import date

ano_nasc = int(input("Ano de nascimento: "))
idade = (date.today().year - ano_nasc)

if 0 <= idade <= 9:
    print(f"MIRIM;\nIDADE: {idade} ano(s)")
elif 10 <= idade <= 14: 
    print(f"INFANTIl;\nIDADE: {idade} anos")
elif 15 <= idade <= 19:
    print(f"JUNIOR;\nIDADE: {idade} anos")
elif 19 < idade <= 20:
    print(f"SÊNIOR;\nIDADE: {idade} anos")
elif idade > 20:
    print(f"MASTER;\nIDADE: {idade} anos")
else:
    print("DIGITE UM VALOR VÁLIDO!!!")