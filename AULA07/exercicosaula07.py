valorN=int(input("Digite um numero inteiro e positivo diferente de 0: "))
soma=0
for i in range(1,valorN+1):
    calcule= 2**i
    soma+=calcule
    print(calcule)
print(f"a soma é {soma}")

   

