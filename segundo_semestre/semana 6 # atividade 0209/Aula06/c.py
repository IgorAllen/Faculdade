import a

nome = str(input('Digite o nome do colaborador: '))
gasto = 0
salariopouco = 0
todos = 0
listadetudo = []

while nome.lower() != 'sair':
    salario = float(input('Digite o salario: '))
    abono = a.calcuoAbono(salario)
    
    if abono < 200:
        abono = 200
        salariopouco += 1

    gasto += salario + abono
    pagamento = salario + abono
    formacao = [nome, pagamento]
    todos += 1
    listadetudo.append(formacao)

    nome = str(input('Digite o nome do colaborador: '))

# Resultados:

print(f'\nProjeção de Gastos com Abono')
print('=' * 30)

for colaborador in listadetudo:
    print(f'Colaborador: {colaborador[0]} -> Salário com Abono: {colaborador[1]}')

print('=' * 30)
print(f'Total de Gastos: {gasto}')
print(f'Foram processados {todos} colaboradores')
print(f'Valor mínimo pago a {salariopouco} colaboradores')

# Modularização

# 