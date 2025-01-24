
lista = [1, 23, 52, 60, 41, 70, 20, 3, 4]
pares = []
impares = []
i = 0
while i < len(lista):
    if lista[i] %2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])
    i = i + 1
print(pares)
print(impares)
