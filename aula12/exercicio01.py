def valorLogico (n):
    if n%2==0:
        return True
    else:
        return False
a = int(input("Digite um numero:"))
print(f"O numero é:{valorLogico(a)} ")
