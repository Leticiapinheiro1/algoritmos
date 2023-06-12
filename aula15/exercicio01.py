arquivo= open("usuarios.txt", encoding= "utf-8")
texto = arquivo.read()
linhas = texto.split("\n")
numeros= []
nomes=[]
for linha in linhas:
    if linha:
        dados = linha.split('-')
    nom=dados[0].strip()
    num = dados[1].strip()  
    nomes.append(nom) 
    numeros.append(num)
print(nomes)
print(numeros)
resultMegabyte=[]
numMemoria=list(map(int,numeros))
mb=1048576
for i in numMemoria:
    megabyte = i/mb
resultMegabyte.append(megabyte)
print(resultMegabyte)
    



