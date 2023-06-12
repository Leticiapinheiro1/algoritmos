import random
frequencia_faces = [0, 0, 0, 0, 0, 0]
for _ in range(6000):
    resultado = random.randint(1, 6)
    frequencia_faces[resultado - 1] += 1

for i in range(6):
    face = i + 1
    frequencia = frequencia_faces[i]
    print(f"Face {face}: {frequencia} vezes")
