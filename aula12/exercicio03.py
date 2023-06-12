def valorPrimo(n):
    contador = 0
    for i in range(1,n+1):
        if (n%i==0):
            contador += 1
    if contador==2:
        return True
    else:
        return False
    
a=int(input("Digite um numero:"))    

print(f"O numero é primo : {valorPrimo(a)}")

cont=0
numer=0

while cont<=50:
    numer+=1
    if valorPrimo(numer)==True:
        print(numer, end="-")   
        cont+=1        









    