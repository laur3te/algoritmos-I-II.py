cores = {'limpa': '\x1b[m',
         'azul': '\x1b[34m',
         'amarelo': '\x1b[33m',
         'roxo': '\x1b[95m'}

frase = str(input("Digite uma frase: ")).upper().strip()
print("Quantidade de letras A: {}{}{}".format(cores['roxo'], frase.count("A"), cores['limpa']))
print("Posição em que a primeira letra A aparece: {}{}{}".format(cores['amarelo'], frase.find("A")+1, cores['limpa']))
print("Posição em que a última letra A aparece: {}{}{}".format(cores['azul'], frase.rfind("A")+1, cores['limpa']))
