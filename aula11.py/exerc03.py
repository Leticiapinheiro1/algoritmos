lista1 = []
lista2 = []

print("Insira os elementos da primeira lista:")
for i in range(10):
    elemento = int(input("Digite um número inteiro: "))
    lista1.append(elemento)

print("Insira os elementos da segunda lista:")
for i in range(10):
    elemento = int(input("Digite um número inteiro: "))
    lista2.append(elemento)

conjunto_uniao = set(lista1).union(lista2)

print("Conjunto de união das duas listas:")
for elemento in conjunto_uniao:
    print(elemento)
