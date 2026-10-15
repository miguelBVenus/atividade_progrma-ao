def verificar_carga(horas):
    if horas >= 40:
        return "Carga completa"
    else:
        return "Carga incompleta"

horas = float(input("Digite o número de horas trabalhadas na semana: "))

print(verificar_carga(horas))