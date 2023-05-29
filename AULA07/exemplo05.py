n = int(input("Entre com numero inteiro positivo: "))
a = 0
b = 1
print(a)
for i in range(1,n):
    print(b)
    a,b = b, a+b
