while True:
    n = int(input("Digite uma valor a ser calculado: "))
    if n<=0:
        print("Valor invalido.Tem que ser > que 0!")
        break    
    if (n==0)or (n==1):
        fatorial=1
    else:
        fatorial=1
    for i in range(1, n+1):
        fatorial *=i
print(f"O valor de {n}! é igual a {fatorial}")



