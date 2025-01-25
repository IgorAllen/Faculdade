
def calculoMedia(nota1, nota2):
    mp = (nota1 + (nota2 * 2)) / 3
    return mp

while True:
    nome = input("Entre com o nome do aluno ou 'sair' para encenrar o programa: ")
    if nome == "sair":
        break
    frequencia = int(input("Frequência: "))
    g1 = float(input("G1: "))
    g2 = float(input("G2: "))
    mp = calculoMedia(g1, g2)

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