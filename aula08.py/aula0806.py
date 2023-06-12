vetor = input("Digite um vetor: ")
vetor = vetor.strip()
if vetor == vetor[::-1]:
    print("O vetor é um palíndromo.")
else:
    print("O vetor não é um palíndromo.")
