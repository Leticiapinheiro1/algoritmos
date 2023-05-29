salario=float(input("Qual o seu salário?R$"))
aumento=float(input("Qual o percentual de aumento?%"))
numero=aumento/100
valor_aumento=salario*numero
novo_salario=valor_aumento+salario
print(f"O valor do aumento é de R$:{valor_aumento:.2f}")
print(f"Seu novo salario é: R${novo_salario:.2f}")