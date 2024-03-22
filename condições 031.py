distancia = float(input("Distância: "))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f"O valor cobrado foi de R${preco:.2f}")