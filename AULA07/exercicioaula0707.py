n = int(input("Digite um numero para ser expoente, que seja inteiro e positivo:"))
b = int(input("digite uma numero para ser a base da exponenciação, que seja inteiro e positivo:"))
exp = 1
soma = 0
while exp <= n:
    e= b ** exp
    print(f"{b} elevado a {exp} é igual a {e}")
    exp += 1
    soma += e
print(soma)



