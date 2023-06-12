pesoMedio=0
alturaMedia=0
imcMaior=0
imcMenor=0
for i in range(1,21):
    peso=int(input("Qual o seu peso em kg?"))
    pesoMedio+=peso/20
    altura=int(input("Qual a sua altura em cm? "))
    alturaMedia+=altura/20
    imc=peso/(altura**2)
    if imc>imcMaior:
        imcMaior=imc
    if i==1:
        imcMenor=imc
    if imc<imcMenor:
        imcMenor=imc
print(pesoMedio)
print(alturaMedia)
print(imcMaior)
print(imcMenor)


