anoNascimento=int(input("Digite o ano de nascimento:"))
anoAtual=int(input("Digite o ano atual:"))
idadeAnos=anoAtual-anoNascimento
idadeMeses=idadeAnos*12
idadeDias=idadeAnos*365
idadeSemanas=idadeDias//7#mostrar numero inteiro usar 2 barras.
print("sua idade é:",idadeAnos,"anos,",idadeMeses,"meses,",idadeDias,"dias, e",idadeSemanas,"semanas.")