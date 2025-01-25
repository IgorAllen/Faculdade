
import random

def jogo():
    while True:
        numero_secreto = random.randint(0, 100)
        tentativas = 0

        while True:
            palpite = int(input("Digite seu palpite: "))
            tentativas = 1 + tentativas

            if palpite == numero_secreto:
                print("-" * 40)
                print(f"Parabéns!!!! O número correto é {palpite}")
                print(f"Quantidade de tentativas --> {tentativas}")
                print("-" * 40)
                break
            elif palpite < numero_secreto:
                print("O número secreto é maior.")
            else:
                print("O número secreto é menor.")
        
        jogar_novamente = input("Jogar novamente? (s/n): ")
        if jogar_novamente != 's':
            break

jogo()

