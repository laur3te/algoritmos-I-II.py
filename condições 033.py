lista = []
for i in range (0, 3):
    num = float(input(f"Insira o {i+1}° valor: "))
    lista.append(num)

maior = lista[0]
menor = lista[0]

for num in lista:
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

print(f"{maior} é o MAIOR valor entre os digitados\n{menor} é o MENOR valor entre os digitados.")
