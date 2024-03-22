cores = {"limpar": "\x1b[m",
         "lilas": "\x1b[95m",
         "azul": "\x1b[34m", 
         "amarelo": "\x1b[33m",
         "vermelho": "\x1b[31m"}

num = int(input("Insira um valor de 0 a 9999: "))
num2 = f"{num:04}" #Número formatado para ter quatro casas

milhar = num2[0]
centena = num2[1]
dezena = num2[2]
unidade = num2[3]

print("Milhar: {}{}{}".format(cores["azul"], milhar, cores["limpar"]))
print("Centena: {}{}{}".format(cores["amarelo"], centena, cores["limpar"]))
print("Dezena: {}{}{}".format(cores["lilas"], dezena, cores["limpar"]))
print("Unidade: {}{}{}".format(cores["vermelho"], unidade, cores["limpar"]))