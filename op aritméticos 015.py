dias = int(input("Quantidade de dias alugados: "))
km = float(input("Quilometragem percorrida: "))
aluguel = (dias*60) + (km*0.15)
print(f"O valor a pagar é R${aluguel:.2f}")