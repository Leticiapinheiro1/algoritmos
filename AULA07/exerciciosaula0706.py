numero=int(input("entre com um numero inteiro e positivo:"))
fatorial=1
if numero <0:
    print("Não existe fatorial")
elif numero ==0:
    print("fatorial =1")
else:
    for i in range(1, numero+1):
        fatorial=fatorial*i
    print(f"fatorial é igual:{fatorial}")                                                                                                                                                                                                               