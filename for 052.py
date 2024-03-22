#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

divisivel = 0 #Contador que irá dizer quantas vezes o número é divisível
num_primo = int(input("Insira um valor: "))

for primo in range (1, num_primo + 1): #+1 irá fazer o número primo também seja analisado.
    if num_primo % primo == 0: 
        print("\x1b[32m", end = " ") #Printa verde os divisíveis.
        divisivel += 1
    else:
        print("\x1b[31m", end = " ") #Printa vermelho os não-divisíveis.
    print(f"{primo}", end = " ") #Imprime todos os número de 1 até num_primo.

if divisivel > 2: #Analisa quantas vezes num_primo foi dividido 
    print(f"\n\x1b[00mO número {num_primo} NÃO é primo, pois foi divisível {divisivel} vezes.")
else:
    print(f"\n\x1b[00mO número {num_primo} é primo, pois foi divisível somente {divisivel} vezes.")
