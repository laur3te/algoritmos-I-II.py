from random import shuffle
alunos = []
for i in range (0,4):
    nome = (str(input("Nome do aluno(a): ")))
    alunos.append(nome)

shuffle(alunos) #Mistura os elementos da lista
print("=-"*10)
print("Ordem sorteada: ")
print(alunos) 