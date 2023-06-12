
while True:
    doisvalores=(input("Digite dois valores sendo o primeiro maior que o segundo. ex: 46-19:"))
    novovalor=doisvalores.split("-")
    m=int(novovalor[0])
    n=int(novovalor[1])

    if m<=n:
            print("erro: m deve ser maior que n. Digite novamente")
            continue
    soma_intervalo=0
    for num in range(n,m+1):
            soma_intervalo+=num
    print(f"a soma do intervalo é:{soma_intervalo}")



  

    




