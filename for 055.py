#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
lista = [] #Armazena os dados inseridos
for peso in range(0, 5):
    massa = float(input(f"Insira o {peso + 1}° peso: "))
    lista.append(massa) 

maior = lista[0] #Para a variável não dar erro, comparamos ela com o primeiro item da lista.
menor = lista[0]

for massa in lista: #Para cada item da lista...
    if massa > maior: #Se o item analisado for o maior, ele atualiza.
        maior = massa
    elif massa < menor: #Se o item analisado for o menor, ele atualiza.
        menor = massa

print("=-"*10)
print(f"Maior peso: {maior}KG\nMenor peso: {menor}KG")
print("=-"*10)
