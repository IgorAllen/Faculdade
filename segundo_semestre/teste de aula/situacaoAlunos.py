while True:
    nome = input("Entre com o nome do aluno ou 'sair' para encenrar o programa: ")
    if nome == "sair":
        break
    frequencia = int(input("Frequência: "))
    g1 = float(input("G1: "))
    g2 = float(input("G2: "))
    mp = (g1 + (g2 * 2)) / 3

    if frequencia < 75:
        print("Reprovado!")
    elif mp >= 6:
        print("Aprovado!")
    else:
        print("Exame Final")
        ef = float(input("Entre com a nota do exame final: "))
        mf = (mp + (ef * 2)) / 3
        if mf >= 6:
            print("Aprovado!")
        else:
            print("Reprovado!")


