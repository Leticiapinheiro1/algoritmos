frase = input("Digite uma frase: ")
frase = frase.lower()
contador_vogais = 0
for caractere in frase:
    if caractere in 'aeiou':
        contador_vogais += 1

print("Quantidade de vogais na frase:", contador_vogais)
