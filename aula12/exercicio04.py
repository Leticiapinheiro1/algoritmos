def anobi (n):
    if n%4==0:
        if (n%100) == 0:
          if (n%400) == 0:
             return True
          else:
             return False
        else:
           return True
    else:
       return False   

n = int(input("Digite o ano:"))     
if anobi(n):
   print("Ano Bissexto") 


