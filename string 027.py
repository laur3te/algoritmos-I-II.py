print("=-"*25)
nome = str(input("Digite seu nome completo: ")).split()
print("=-"*25)

primeiro_nome = nome[0]
ultimo_nome = nome[-1]

print("Primeiro nome: \x1b[95m{}\x1b[00m\nÚltimo Nome: \x1b[96m{}\x1b[00m".format(primeiro_nome, ultimo_nome))