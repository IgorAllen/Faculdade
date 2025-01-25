# 6. Função que ordena valores em ordem crescente
def ordenar_valores():
    v1 = int(input("Digite o valor 1: "))
    v2 = int(input("Digite o valor 2: "))
    v3 = int(input("Digite o valor 3: "))
    valores = [v1, v2, v3]
    valores.sort()
    return ",".join(map(str, valores))
