from math import sin, cos, tan, radians
ang = float(input("Insira o ângulo: "))
sin = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print(f"O SENO de {ang:.0f}° é {sin:.3f}\nO COSSENO de {ang:.0f}° é {cos:.3f}\nA TANGENTE de {ang:.0f}° é {tan:.3f}")