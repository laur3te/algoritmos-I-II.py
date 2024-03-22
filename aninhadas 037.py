#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
#1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Insira um valor: "))
print('''[ 1 ] Binário\n[ 2 ] Octal\n[ 3 ] Hexadecimal''')
base_conversao = int(input("Opção: "))

if base_conversao == 1:
    binario = bin(num)
    print(f"A representação binária do {num} é \x1b[92m{binario}\x1b[00m")
elif base_conversao == 2:
    octal = oct(num)
    print(f"A representação octal do {num} é \x1b[94m{octal}\x1b[00m")
elif base_conversao == 3: 
    hexadecimal = hex(num)
    print(f"A representação hexadeximal do {num} é \x1b[96m{hexadecimal}\x1b[00m")
else:
    print("Digite uma opção VÁLIDA!")
    
#Quando usamos "OR" devemos repetir a variável para obter uma resposta correta para a condição.
#Quando não usamos corretamente, a string sempre será verdadeira. 
    