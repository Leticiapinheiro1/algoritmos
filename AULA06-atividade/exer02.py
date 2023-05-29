valor_compra=float(input("Digite o valor da compra:"))
if valor_compra<=1000:
    desconto=valor_compra*0.1
elif valor_compra<=5000:
    desconto=valor_compra*0.2
else:
    desconto=valor_compra*0.3
valor_total= valor_compra - desconto
print(f"O valor da compra é de R${valor_compra:.2f}.")
print(f"O desconto é de R${desconto:.2f}")
print(f"O valor final com desconto é de R${valor_total:.2f}")
