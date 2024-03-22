#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

tabuada = int(input("Insira um valor: "))
for c in range (0, 11):
    print(f"{tabuada} x {c} = {tabuada*c}")
