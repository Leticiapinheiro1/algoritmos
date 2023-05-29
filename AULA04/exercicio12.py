from math import sqrt
degrau=float(input("Digite a altura dos degraus em cm:"))

altura=float(input("Qual a altura que deseja subir? em metros:"))

distancia=float(input("Qual a distância que escada ficará da onde deseja subir?"))

altura_emCm=altura*100

distancia_emCm=distancia*100

altura_escada=altura_emCm**2 + distancia_emCm**2

altura_escadaFinal=sqrt(altura_escada)

alt_degraus=altura_escadaFinal/degrau

print(f"Serão necessarios: {alt_degraus:.2f} degraus")


