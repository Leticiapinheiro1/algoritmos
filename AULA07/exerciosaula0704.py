soma=0
contador=0
for i in range(1,1000):
    numero=int(input("Digite um numero: "))
    if numero==0:
        print("saiu do lopping")
        break
    elif numero % 2 == 0:
        soma+=numero
        contador+=1
    else:
        numero%2!=0
        continue

media=soma/contador
print(media)


    
    
    

    

        

    

