from random import choice
alunos = []
for i in range(0, 4):
    nome = str(input("Nome do aluno(a): "))
    alunos.append(nome)

escolhido = choice(alunos) #Escolhe um elemento da lista
print("=-"*10)
print(f"O aluno escolhido foi {escolhido}")
