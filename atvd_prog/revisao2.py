
def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media


quantidade = int(input("Digite a quantidade de notas: "))
notas = []

for i in range(quantidade):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)
 
resultado = calcular_media(notas)

print("A média do aluno é:", resultado)
