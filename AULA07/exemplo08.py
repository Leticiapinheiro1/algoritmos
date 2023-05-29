

base = float(input("Digite o valor da base do triângulo: "))
while base<=0:
    base= float(input("Digite o valor da base do triângulo >0:"))

while True:
 altura = float(input("Digite o valor da altura do triângulo: "))
 if altura>0:
     break
area = (base*altura)/2
input(f"Area é:{area:.2f}")



