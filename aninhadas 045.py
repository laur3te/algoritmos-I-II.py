#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

print("\x1b[95m= - =\x1b[00m"*7)

itens = ("PEDRA", "PAPEL", "TESOURA")
maquina = randint(0, 2)
jogador = int(input('''[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\nOpção: '''))

print("\x1b[95m= - =\x1b[00m"*7)

print("JO")
sleep(0.5)
print("     KEN")
sleep(0.5)
print("             PÔ")
sleep(0.5)
print("\x1b[95m. . . \x1b[00m"*6)

if maquina == 0:
    if jogador == 0:
        print(f"\x1b[33mEMPATE!\x1b[00m\n{itens[jogador]} VS {itens[maquina]}")
    elif jogador == 1:
        print(f"\x1b[32mVITÓRIA\x1b[00m\n{itens[jogador]} VS {itens[maquina]}")
    elif jogador == 2:
        print(f"\x1b[31mMÁQUINA GANHOU!\x1b[00m\n{itens[jogador]} VS {itens[maquina]}")

elif maquina == 1:
    if jogador == 0:
        print(f"\x1b[31mMÁQUINA GANHOU!\x1b[00m\n{itens[jogador]} VS {itens[maquina]}")
    elif jogador == 1:
        print(f"\x1b[33mEMPATE!\x1b[00m\n{itens[jogador]} VS {itens[maquina]}")
    elif jogador == 2:
        print(f"\x1b[32mVITÓRIA\x1b[00m\n{itens[jogador]} VS {itens[maquina]}")

elif maquina == 2:
    if jogador == 0:
        print(f"\x1b[32mVITÓRIA\x1b[00m\n{itens[jogador]} VS {itens[maquina]}")
    elif jogador == 1:
        print(f"\x1b[31mMÁQUINA GANHOU!\x1b[00m\n{itens[jogador]} VS {itens[maquina]}")
    elif jogador == 2:
        print(f"\x1b[33mEMPATE!\x1b[00m\n{itens[jogador]} VS {itens[maquina]}")

else:
    print("OPÇÃO INVÁLIDA!")
