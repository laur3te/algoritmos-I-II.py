print("=-"*15)
print("Analisando triângulos")
print("=-"*15)
a = float(input("Informe o valor do 1° lado: "))
b = float(input("Informe o valor do 2° lado: "))
c = float(input("Informe o valor do 3° lado: "))

if (abs(b - c) < a < b + c) and (abs(a - c) < b < a + c) and (abs(a - b) < c < a + b): 
    print("Os valores digitados FORMAM um triângulo!")
else:
    print("Os valores digitados NÃO FORMAM um triângulo!")