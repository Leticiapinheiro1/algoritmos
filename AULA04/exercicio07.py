deposito=float(input("Qual o valor do depósito:R$"))
taxa_de_juros=float(input("Qual a taxa de juros:%"))
numeroTaxa=taxa_de_juros/100
rendimento=deposito*numeroTaxa
valor_total= rendimento+deposito
print("Seu rendimento foi de R$:",rendimento)
print(f"Seu valor atualizado é R$:{valor_total:.2f}")