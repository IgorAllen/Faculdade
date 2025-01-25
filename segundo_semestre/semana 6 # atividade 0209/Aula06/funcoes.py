def calcula_abono(salario):
    abono = salario * 0.25
    if abono < 200:
        abono = 200
    
    return abono