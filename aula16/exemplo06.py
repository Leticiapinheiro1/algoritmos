def entrada( ):
    try:
        num= int(input("informe um numero:"))
    except:
        return None    
    else:
        return num
    finally:
        print("Fim do bloco")
a=entrada
print (a)
