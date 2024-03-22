#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = input("Insira uma frase: ").replace(" ", "").upper() #Replace substítui a função .strip por não conseguir separar a frase corretamente. 

for c in frase: #Itinera todos os itens de C.
    continue #Continue preenche o loop para evitar erros.

frase_reversa = frase[::-1] #[::-1] representa a inversão da cadeia de string.
print(f'A frase reversa: {"-".join(frase_reversa)}', end = " ") #.join junta todos os elementos presentes com um hífen.

if frase_reversa == frase:
    print(f"é um palíndromo.")
else: 
    print(f"não é um palíndromo.")
