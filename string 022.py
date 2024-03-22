print("\x1b[94m", "=-"*20, "\x1b[00m")
nome = str(input("Nome completo: "))
print("\x1b[94m", "=-"*20, "\x1b[00m")

print("UPPER: ","\x1b[96m", nome.upper(), "\x1b[00m")
print("LOWER: ","\x1b[95m", nome.lower(), "\x1b[00m")

sem_espaço = nome.replace(" ", "")
print("SEM ESPAÇO: ","\x1b[92m", len(sem_espaço), "\x1b[00m")

primeiro_nome = nome.split()
print("CONTAGEM DO PRIMEIRO NOME: ", "\x1b[93m" ,len(primeiro_nome[0]), "\x1b[00m")