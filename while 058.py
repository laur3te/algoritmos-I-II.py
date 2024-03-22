from random import randint #Usado para sortear o valor inteiro

contador = 0 
num_sugerido = None #Usado como sentinela e garante que o loop seja realizado pelo menos uma vez.
num_aleatorio = randint(0, 10)

while num_sugerido != num_aleatorio: 
    contador += 1 #Conta quantas tentativas o usuário fez.
    num_sugerido = int(input("Sugestão: "))

    if num_sugerido == num_aleatorio:
        print("\x1b[36m- \x1b[00m"*15)
        print(f"\x1b[32;1mPARABÉNS, VOCÊ ACERTOU!\x1b[00m\nO número da vez foi: {num_aleatorio}")
        print("\x1b[36m- \x1b[00m"*15)
    else:
        print("\x1b[31mTente novamente!\x1b[00m")

print(f"Foi(ram) feita(s) \x1b[36;1m{contador}\x1b[00m tentativa(s) para acertar o número.")