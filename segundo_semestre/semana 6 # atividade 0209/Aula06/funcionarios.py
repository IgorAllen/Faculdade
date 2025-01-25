import funcoes

colaboradores = []
salarios = []
total_salarios = 0
qt_abonos_minimo = 0

while True:
    colaborador = input("Entre com o nome do colaborador (ou sair para encerrar): ")
    if colaborador == "sair":
        break

    salario = float(input("Entre com o salário do colaborador: "))

    # Adicionando valores às listas
    colaboradores.append(colaborador)
    salarios.append(salario)


for i in range(len(colaboradores)):
    abono = funcoes.calcula_abono(salarios[i])
    salario_colaborador = salarios[i] + abono
    print(f"{colaboradores[i]} -> Total: {salario_colaborador}")

    # Somatório de salários
    total_salarios += salario_colaborador

    # Quantidade de abonos pagos com o valor minímo (200)
    if abono <= 200:
        qt_abonos_minimo += 1

print(f"Foram processados {len(colaboradores)} colaboradores")
print(f"Valor mínimo pago a {qt_abonos_minimo} colaborador(es).")