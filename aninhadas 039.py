#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_nas = int(input("Ano de nascimento: "))
idade = (date.today().year - ano_nas)
sexo = str((input("F/M? "))).upper()

if sexo == "M":
    if idade == 18: 
        print("Hora de se alistar.")
    elif idade > 18:
        print("Já passou do tempo de se alistar.")
        print(f">> JÁ SE PASSOU(RAM) {idade - 18} ANO(S).")
    else:
        print("Ainda falta tempo para se alistar.")
        print(f">> FALTA(M) {18 - idade} ANO(S).")
if sexo == "F":
    print("O alistamento militar não é obrigatório para mulheres.")