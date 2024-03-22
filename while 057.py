sexo = "F" 
while sexo == "M" or sexo == "F":
    sexo = str(input("[F/M]: ")).upper().strip()
    
    if sexo != "M" and sexo != "F":
        print("Opção inválida! \n[F - Feminino // M - Masculino]")
        sexo = str(input("[F/M]: ")).upper().strip()
