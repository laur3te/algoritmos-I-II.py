from math import floor

num = floor(float(input("Insira um valor: ")))
if num % 2 == 0:
    print(f"{num} é PAR!")
else: 
    print(f"{num} é IMPAR!")
