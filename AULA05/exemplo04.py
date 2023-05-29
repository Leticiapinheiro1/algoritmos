print('Calculo de peso ideal')
sexo=input("entre com seu sexo (M) OU (F): ")
altura=float(input("Entre com sua altura em metros: "))
if sexo.upper()== "M":
    peso = (72.7*altura) - 58
else:
    peso=(62.1*altura) - 44.7
print (f"seu peso ideal é {peso:.1f} kg.")







