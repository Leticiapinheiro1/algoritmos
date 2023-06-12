data=input("Qual a sua data de aniversario? dd/mm/aaaa:")
dia = data[:2]
mes = data[3:5]
ano = data[6:10]
data_formato_novo = ano + mes + dia

print("Data no formato AAAAMMDD:", data_formato_novo)