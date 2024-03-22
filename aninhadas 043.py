#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso. Entre 18,5 e 25: Peso Ideal. 25 até 30: Sobrepeso. 30 até 40: Obesidade. Acima de 40: Obesidade Mórbida
print("\x1b[95m=-\x1b[00m"*10)

peso = float(input("Peso: "))
alt = float(input("Altura: "))
imc = peso/(alt**2)

print("\x1b[95m=-\x1b[00m"*10)

if imc <= 18.5:
    print(f"IMC: {imc:.1f}\n\x1b[32mABAIXO DO PESO\x1b[00m")
elif 18.5 <= imc <= 25:
    print(f"IMC: {imc:.1f}\n\x1b[94mPESO IDEAL\x1b[00m")
elif 25 < imc <= 30:
    print(f"IMC: {imc:.1f}\n\x1b[31mSOBREPESO\x1b[00m")
elif 30 < imc <= 40:
    print(f"IMC: {imc:.1f}\n\x1b[36mOBESIDADE\x1b[00m")
else: 
    print(f"IMC: {imc:.1f}\n\x1b[35mOBESIDADE MÓRBIDA\x1b[00m")
