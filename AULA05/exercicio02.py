a= float(input("Digite a primiera nota: "))
b= float(input("Digite a segunda nota: "))
c= float(input ("Digite a terceira nota: "))
media= (a+b+c)/3
if media>=7:
    print (f"sua média é {media:.1f}.Aprovado!")
else:
    if media >=3:
        print(f"Sua media é {media:.1f}. Exame!")
        nota = 12 - media
        print(f"Você precisa tirar o minimo de nota: {nota:.1f}")
    else:
        print(f"Sua média é {media:.1f}.Reprovado!")