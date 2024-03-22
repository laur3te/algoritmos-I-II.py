#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais. ISÓSCELES: dois lados iguais, um diferente. ESCALENO: todos os lados diferentes
print("\x1b[95m=-\x1b[00m"*20)

lado1 = float(input("Informe o valor do 1° lado: "))
lado2 = float(input("Informe o valor do 2° lado: "))
lado3 = float(input("Informe o valor do 3° lado: "))

print("\x1b[95m=-\x1b[00m"*20)

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2: 
    print("Os valores digitados \x1b[96mFORMAM\x1b[00m um triângulo", end = " ")
    if lado1 == lado2 == lado3:
        print("\x1b[32mEQUILÁTERO\x1b[00m")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("\x1b[33mISÓSCELES\x1b[00m") 
    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        print("\x1b[31mESCALENO\x1b[00m")
else:
    print("Os valores digitados \x1b[95mNÃO FORMAM\x1b[00m um triângulo!")