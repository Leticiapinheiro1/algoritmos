import math
e=0
n=int(input("digite um numero inteiro positivo: "))
b=int(input("digite o valor da base: "))
i= 1
while i<=n:
    e= e + math.pow(b,i)
    i=i+1
print (f"O valor de e= {e:.2f}")



