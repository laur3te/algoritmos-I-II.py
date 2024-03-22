#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print("="*14)
print("TERMOS DA P.A")
print("="*14)

primeiro_termo = int(input("1° TERMO: "))
razao = int (input("RAZÃO: "))
print("="*14)

for pa in range (1, 11):
    resposta = primeiro_termo + (pa - 1) * razao
    print(f"{pa}° TERMO = {resposta}")
