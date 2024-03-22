#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

cont = 0 
lista = [] #A lista armazena as idades inseridas no programa.
soma = 0 #Somátoria para a realização da média entre as idades.
idade_homem_velho = 0 
nome_homem_velho = ''

for i in range (4):
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("F/M: ")).strip().upper() #.upper() para filtrar a entrada de dados e evitar erro em sensitive case.
    print("=-"*7)

    lista.append(idade)
    soma += idade

    if idade < 20 and sexo == "F": #Contabiliza a quant de mulheres com idade inferior a 20.
        cont += 1 

    if idade > idade_homem_velho and sexo == "M": #Analisa os elementos em busca do homem de maior idade.
        nome_homem_velho = nome #Guarda o nome do homem mais velho.
        idade_homem_velho = idade #Guarda a idade do homem mais velho.

media = sum(lista) / 4 #len(lista) seria a melhor opção se não soubessemos a quantidade de dados.
print(f"> A média entre idade é de {media:.2f}.")

print(f"> Homem mais velho: {nome_homem_velho} - Idade: {idade_homem_velho} anos.")

print(f"> Há {cont} mulher(res) com menos de 20 anos.")
