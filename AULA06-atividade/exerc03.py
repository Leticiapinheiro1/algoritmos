# Dimensões do cômodo e da porta
altura_pé_direito=2.8
largura= float((input("Digite a largura do cômodo em metros:")))
comprimento=float(input("Digite o comprimento do cômodo em metros:"))
area_porta=0.8*2.1
a=3.6
b=1
c=18
print(input("Digite (a)-lata de 3.6 litro (b)-lata de 1 litros e (C)lata de 18 litros:"))

# Calculando as areas da paredes - desconsiderando a porta
area_paredes= (2*altura_pé_direito*(largura+comprimento))- area_porta

# Calculando quantidae de tinta
qtd_tinta=area_paredes/3

#Calculando a quantidade de latas (litros)
latas=b,c
if latas:
    qtd_latas=qtd_tinta/b
    qtd_latas=qtd_tinta/c
print(f"Quantidade de latas de tintas necessárias:{qtd_latas:.2f} ")
