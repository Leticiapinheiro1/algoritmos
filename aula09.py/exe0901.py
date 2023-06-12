numeros= []
for i in range(10):
    elemento = int(input("Digite um número inteiro: "))
    numeros.append(elemento)
    
print(numeros)

numeros_invertido =numeros[::-1]
print(f"Numeros na ordem inversa:{numeros_invertido}")
