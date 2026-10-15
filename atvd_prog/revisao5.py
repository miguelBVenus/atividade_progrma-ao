def alunos_aprovados(notas):
    aprovados = []

    for nota in notas:
        if nota >= 7:
            aprovados.append(nota)

    return aprovados


notas = [8, 5, 7, 6, 9, 4, 7.5]

print(alunos_aprovados(notas))