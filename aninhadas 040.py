#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = float(input("Insira a 1° nota: "))
nota2 = float(input("Insira a 2° nota: "))
media = (nota1 + nota2) / 2

if media < 5.0: 
    print(f"Sua média foi de {media:.1f}\n\x1b[31m>> REPROVADO\x1b[00m")
elif 5.0 <= media < 7: 
    print(f"Sua média foi de {media:.1f}\n\x1b[33m>> RECUPERAÇÃO\x1b[00m")
else:
    print(f"Sua média foi de {media:.1f}\n\x1b[32m>> APROVADO\x1b[00m")
    