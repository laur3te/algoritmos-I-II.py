from math import hypot
oposto = float(input("Insira o comprimento do cateto oposto: "))
adjacente = float(input("Insira o comprimento do cateto adjacente: "))
hipotenusa = hypot(oposto, adjacente)
print(f"A hipotenusa do triângulo retângulo é {hipotenusa:.2f}")