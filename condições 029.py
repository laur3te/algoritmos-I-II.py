velocidade = int(round(float(input("Velocidade: "))))
if velocidade >= 80:
    multa = (velocidade - 80) // 10 * 7
    print(f"Você foi multado por excesso de velocidade.\nSua multa é de R${multa:.2f}")
else: 
    print("Limite não ultrapassado!")