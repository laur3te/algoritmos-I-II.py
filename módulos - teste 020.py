from random import shuffle
carrinho = []
for i in range (0, 4):
    comprar = str(input("Insira os alimentos que precisa comprar: "))
    carrinho.append(comprar)

shuffle(carrinho) #Embaralha a lista
print("A ordem em que devo comprar é: ")
print(carrinho) 