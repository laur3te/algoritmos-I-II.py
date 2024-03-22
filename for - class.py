'''
for kawaii in range(1000, 0, -100): #Começa a contar de 1000 até o 0, tirando -100 a cada repetição.
    print(kawaii)
print('FIM')
'''
#INÍCIO / FIM / PASSO 
#(0, 100, 5)

inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
for kawaii in range(inicio, fim, passo): 
    print(kawaii)
print("Fim")