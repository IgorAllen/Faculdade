inteiros = [-2, 22, 11, -8, 9, 10, -45, 20, 34]


num = int(input("Digite um número inteiro: "))
while num != 0:
    inteiros.append(num)

positivos = []

i = 0
while i < len(inteiros):
    if inteiros[i]>0:
        positivos.append(inteiros[i])
    i = i + 1
print('Lista dos números positivos: ', positivos)

negativos = []

i = 0
while i < len(inteiros):
    if inteiros[i]<0:
        negativos.append(inteiros[i])
        soma_neg = soma_neg + inteiros[i]
    i = i + 1

print('Lista dos números negativos: ', negativos)
print('A soma dos números negativos é: ', soma_neg)

numeros_pares = []

i = 0
while i < len(inteiros):
    if inteiros[i]<0:
        numeros_pares.append(inteiros[i])
    i = i + 2

print("Numeros da posição par", numeros_pares)