nome = str(input("Qual é seu nome? "))
if nome == "Laura":
    print("Que nome bonito!", end= " ")
elif nome == "Maria" or nome == "Gabriel" or nome == "Ana":
    print("Seu nome é bem popular no Brasil.", end = " ")
elif nome in "Nayara Sabrina Gabriela Catarina":
    print("Que belo nome feminino!!", end = " ")
else:
    print("Seu nome é normal.", end = " ")
print(f"Tenha um bom dia, {nome}.")