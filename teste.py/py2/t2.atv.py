"""
num = int(input('Digite o número:'))

lista = []
contador = 1

while contador <= num:
    lista.append(contador)
    contador = contador + 1
print(lista)
"""
"""
lista = [1, 2, 3, 4, 5]

lista_reversa = []
i = len(lista) - 1
while i >= 0:
    lista_reversa.append(lista[i])
    i = i - 1
print(lista_reversa)
"""
"""
lista1 = [1, 3, 5]
lista2 = [2, 4, 6]
lista_intercalada = []
i = 0
while i < len(lista1):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])
    i = i + 1
print(lista_intercalada)
"""
lista = [1, 2, 3, 4, 5, 6]

soma_pares = 0
contador_pares = 0
i = 0
while i < len(lista):
    if lista[i] % 2 == 0:
        soma_pares = soma_pares + lista[i]
        contador_pares = contador_pares + 1
        media = soma_pares / contador_pares
    i = i + 1
    
print(media_pares)


