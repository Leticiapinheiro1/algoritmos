string_numerica = input("Digite os nove caracteres numéricos: ")
if len(string_numerica) != 9 or not string_numerica.isnumeric():
    print("Entrada inválida!")
else:
    parte_inteira = string_numerica[:6]
    parte_decimal = string_numerica[6:]

    parte_inteira_formatada = '.'.join(parte_inteira[i:i+3] for i in range(0, 6, 3))

    parte_decimal_formatada = parte_decimal[:2] + ',' + parte_decimal[2:]

    string_formatada = parte_inteira_formatada + ',' + parte_decimal_formatada

    print("Mostrado:", string_formatada)