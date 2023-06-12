from funcoes import jogadores
r=""
while r!= "n":
    print("Vamos jogar dados!")
    input("Aperte enter para sortear o valor:")
    eu = jogadores()
    print(f"seu numero é :{eu}")
    input(f"Aperte enter para que eu possa jogar")
    pc = jogadores()
    print(f"Meu numero é {pc}")

    if eu > pc:
        print("você ganhou!!")
    elif eu == pc:
        print("Empatamos")
    else:
        print("Eu ganhei!!")
    r = input("quer jogar novamente s/n?")  







