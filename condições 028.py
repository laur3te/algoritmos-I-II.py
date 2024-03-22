from random import randint
from time import sleep

print("=-"*20)
print("Adivinhe o número!\n""DICA: Está entre 0 e 5")
print("=-"*20)

num_aleatorio = randint(0, 5)
num_sugerido = int(input("Sugestão: "))
if num_aleatorio == num_sugerido:
    print("> > > PROCESSANDO. . .")
    sleep(3)
    print("VOCÊ GANHOU! :)")
else: 
    print("> > > PROCESSANDO. . .")
    sleep(3)
    print(f"VOCÊ PERDEU! :(\nO número escolhido foi {num_aleatorio}.")
