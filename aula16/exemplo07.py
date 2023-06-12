def divisão (a,b):
    try:
        return int (a)/int(b)
    except (ValueError, ZeroDivisionError) as erro:
        return f"Ocorreu um outro problema!"
n1= int(input("informe o dividendo:"))
n2= int(input("informe oo divisor:"))
print (divisão(n1,n2))
