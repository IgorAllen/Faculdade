def somaNumeros(*args):
    soma = 0
    for numero in args:
        soma = soma + numero
    return soma

print(somaNumeros(1, 2, 3, 4, 5))