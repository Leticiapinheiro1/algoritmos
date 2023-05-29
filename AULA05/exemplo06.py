print ("tipo de triângulo")
a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))
c= int(input("Digite um valor para c: "))
if ((a+b)>c) and ((a+c)>b) and ((b+c)>a):
    print("Os lados formam um triângulo!")
    if((a==b)and(b==c)):
        print ("Triângulo Equilatero")
    elif (a==b) or (b==c) or (a==c):
        print("Triângulo isóceles!")  
    else:
        print("Triângulo escaleno!") 
else:
    print ("Os lados informados nao foram um triângulo!")           

   
