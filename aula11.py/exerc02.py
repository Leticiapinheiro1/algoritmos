
dados = {}
for i in range(10):
    sobrenome = input("Digite o sobrenome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    dados[sobrenome] = idade

maior_idade = 0
sobrenome_maior_idade = ""

for sobrenome, idade in dados.items():
    if idade > maior_idade:
        maior_idade = idade
        sobrenome_maior_idade = sobrenome

print(f"Sobrenome da pessoa com maior idade: {sobrenome_maior_idade}")
