def numeroMaisFrequente(numero):
    numeroMaisFrequente = None
    maiorFrequencia = 0
    for numero in numeros:
        frequencia = numeros.count(numero)
        maiorFrequencia = frequencia
        numeroMaisFrequente = numero

    return(maiorFrequencia, maiorFrequencia)

listaNumeros = [1, 2, 3, 4, 5, 6, 1]
(numeroMaisFrequente, frequecia) = numeroMaisFrequente(listaNumeros)

print(f'O numero que mais apareceu é o {numeroMaisFrequente} e a quantidade de vezes foram {frequecia} vezes')