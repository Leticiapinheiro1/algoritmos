
numeros1= []
numeros2=  []
for i in range(10):
    num = int(input("Digite um número inteiro: "))
    numeros1.append(num)
print(numeros1)      
for i in range(10):
    nu = int(input("Digite um número inteiro: "))
    numeros2.append(nu)
numerosRes= []
for i in range (10):
    numerosRes.append(numeros1[i])
    numerosRes.append(numeros2[i])
print(numeros1)
print(numeros2) 
print(numerosRes)

