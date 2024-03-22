sal = float(input("Informe o salário: "))
if sal > 1250:
    superior_sal = sal * 0.10
    print(f"O seu salário sofreu 10% de aumento!\nValor atualizado: R${superior_sal + sal:.2f}")
else:
    inferior_sal = sal * 0.15
    print(f"O seu salário sofreu 15% de aumento!\nValor atualiazado: R${inferior_sal + sal:.2f}")
