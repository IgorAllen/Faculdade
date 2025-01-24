import random

numero_aleatorio = random.randint(1, 10)

print("Bem-vindo ao jogo Adivinhe o Número!")
print("Tente adivinhar o número entre 1 e 10.")

tentativas = 0
adivinhou = False

while adivinhou == False:

    tentativa = int(input("Digite sua tentativa: "))
    tentativas += 1

    if tentativa == numero_aleatorio:
        print(f"Parabéns! Você acertou o número {numero_aleatorio} em {tentativas} tentativas!")
        adivinhou = True
    elif tentativa < numero_aleatorio:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
