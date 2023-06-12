
elementos = []
for i in range(10):
    elemento = int(input("Digite um número inteiro: "))
    elementos.append(elemento)

tupla = tuple(elementos)
print("Tupla na ordem inversa:")
for elemento in reversed(tupla):
    print(elemento)