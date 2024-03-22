lista = []
for i in range (0,3): 
    num = int(input("Número: "))
    lista.append(num)

lista.sort()
print(f"O menor número é {lista[0]}\nO maior número é {lista[-1]}")