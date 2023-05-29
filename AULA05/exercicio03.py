a=float(input("Digite um numero:"))
b=float(input("Digite outro numero:"))
opcao=float(input("Escolha uma operação:\n1-Média entre os numeros\n2-Diferença do maior pelo menor \n3-Produto entre os numeros\n4-Divisão do primeiro pelo segundo: "))
if opcao==1:
    media=(a+b)/2
    print(f"Média:{media}")
elif opcao==2:
    if a>b:
        difer=a-b
        print(f"A diferenca é:{difer}")
    else:
        difer=b-a    
        print(f"A diferenca é:{difer}")
elif opcao==3:
    produto=a*b 
    print(f"O produto entre a e b é:{produto}")
elif opcao==4:
    if b!=0:
        div=a/b
        print(f"A divisao entre a e b é:{div}")
    else:
        print("Não é possivel dividir")
else:
    print("Erro!Escolha de 1 a 4")

