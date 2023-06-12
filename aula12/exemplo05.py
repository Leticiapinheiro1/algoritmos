def segundos (h,m,s,):
    return(h *3600 + m *60+ s)

hora=input("Informe a hora do momento em: (horas : minutos : segundos):")
h=hora.split(":")
seg= segundos(int(h[0]), int(h[1]),int(h[2]))
print(f"O total é{seg}segundos!")



