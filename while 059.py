from time import sleep 
num1 = float(input("Insira o 1° valor: "))
num2 = float(input("Insira o 2° valor: "))

titulo = "M E N U" #Temos que definir o título em uma variável para podermos centralizar.
maior = 0 

while True: #Enquanto verdadeiro: 
    print("\x1b[35m✦ \x1b[00m"*10)
    print(f"{titulo.center(19)}") #Título centralizado 
    print("\x1b[35m✦ \x1b[00m"*10)
    print("[ 1 ] ➭ SOMAR")
    print("[ 2 ] ➭ MULTIPLICAR")
    print("[ 3 ] ➭ MAIOR")
    print("[ 4 ] ➭ NOVOS NÚMEROS")
    print("[ 5 ] ➭ SAIR DO PROGRAMA")

    opcao = int(input("Opção.: "))

    if opcao == 1:
        print(f"A SOMA entre {num1} e {num2} é \x1b[35;1m{num1 + num2:.2f}\x1b[00m")
        print("- "*10)
    elif opcao == 2:
        print(f"O PRODUTO entre {num1} e {num2} é \x1b[35;1m{num1 * num2:.2f}\x1b[00m")
        print("- "*10)
    elif opcao == 3:
        if num1 > num2: #Se num1 maior que o num2
            maior = num1 #A variável maior é atualizada com o valor de num1
        else:
            maior = num2 #Se não, maior ganha o valor de num2
        print(f"O MAIOR número entre {num1} e {num2} é \x1b[35;1m{maior}\x1b[00m")
        print("- "*10)
    elif opcao == 4:
        num1 = float(input("Insira um 1° novo valor: "))
        num2 = float(input("Insira um 2° novo valor: "))
    elif opcao == 5:
        print("FINALIZANDO. . .")
        sleep(2)
        print("- "*10)
        break
    else:
        print("\x1b[31;1mOpção inválida!\x1b[00m")
        print("- "*10)
