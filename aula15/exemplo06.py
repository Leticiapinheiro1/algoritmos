arquivo=open("frutas.txt", "a", encoding="utf-8")
while True:
    fruta=input('Digite uma fruta:')
    if fruta=="sair":
            break
    else:
        arquivo.write(fruta)
        arquivo.write('\n')