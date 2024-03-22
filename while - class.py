n = 1
par = impar = 0
while n != 0:
    n = int(input("Valor: "))
    if n != 0: #Desconsidera o zero como um número par e torna-o somente ponto de parada.
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f"Você digitou {par} números pares e {impar} números ímpares!")
