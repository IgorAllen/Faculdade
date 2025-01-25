#Escreva um programa que solicite ao usuário um número inteiro positivo e, em seguida, faça uma contagem regressiva a partir desse número até zero.

'''num = int(input("Solicite o número:"))

# Verifica se o número é positivo
if num <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    # Inicia a contagem regressiva a partir do número fornecido pelo usuário
    print("Contagem regressiva a partir de", num)
    while num >= 0:
        print(num)
        num -= 1
'''
#Crie um programa que gere um número aleatório entre 1 e 100. Em seguida, peça ao usuário para adivinhar o número. Forneça dicas ao usuário ("maior" ou "menor") até que ele adivinhe corretamente.

'''

print("Bem-vindo ao jogo Adivinhe o Número!")
print("Tente adivinhar o número entre 1 e 100.")
print("Vamos Começar...")


num_aleatorio = random.randint(1, 1000)

dica1 = input('É um número entre 1 e 1000:')

while dica1 == num_aleatorio:
    print("Você acertou!!!")'''

#=============================================================================================================================
import random

dica1 = input('É um número entre 1 e 1000:')
aleatorio = random.randint(1, 1000)


tentativa = False 

while dica1 == aleatorio:
    print("Você acertou!!!")
    dica1 = dica1 + 1
else:
    print("Vamos tentar novamente")
