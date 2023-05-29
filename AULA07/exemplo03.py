import math
e = 0
n = int(input("Digite um numero inteiro positivo: "))
for i in range(1,n+1):
    e = e + math.pow(2,i)
    print(f"o valor de e = {e:.2f}")