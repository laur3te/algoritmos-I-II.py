from random import choice
planetas = []
for i in range (0, 5):
    nome = str(input("Informe o nome do planeta: "))
    planetas.append(nome)

print("=-"*10)
sorteio = choice(planetas) #Sorteia um elemento da lista
print(sorteio)