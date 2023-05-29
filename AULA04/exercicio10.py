from math import sqrt
numero=int(input("Digite um numero:"))
if numero>0:
    numero1=numero**2
    numero2=numero**3
    numero3=sqrt(numero)
    print(f"Numero ao quadrado:{numero1}, Numero ao cubo:{numero2},Raiz quadrada:{numero3:.2f}")
else:
    print("Digite outro numero")