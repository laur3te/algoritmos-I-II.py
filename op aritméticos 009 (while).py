num = int(input("INSIRA O NÚMERO DA TABUADA: "))
cont = -1

while cont <= 9:
    cont +=1 
    resposta = num * cont
    print(f"{num} * {cont} = {resposta}")

