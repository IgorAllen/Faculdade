numeros_inteiros = [5, -10, 15, -20, 25, 30, -35, 40]

num = int(input('Digite um número inteiro( 0 para parar): '))
if num != 0:
    numeros_inteiros.append(num)
else:
    print("paramos")

media_pares = 0
pares = []
impares = []
i = 0

while i < len(numeros_inteiros):
    if numeros_inteiros[i] %2 == 0:
        pares.append(numeros_inteiros[i])
    else:
        impares.append(numeros_inteiros[i])
    i = i + 1

soma_pares = 0
i = 0

while i < len(numeros_inteiros):
    if numeros_inteiros[i] %2 == 0:
        soma_pares = soma_pares + numeros_inteiros[i]
    i = i + 1

print(pares)
print(impares)
print(soma_pares)
