
def calculaMedia():


    total = 0
    contador = 0
    

    while contador < 5:
        num = int(input("Digite um número: "))
        total += num
        contador = 1 + contador
    

    media = total / 5
    print("A média dos números é:", media)
    return media


calculaMedia()

