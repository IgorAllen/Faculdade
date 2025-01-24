"""i = 10

while i <= 100:
    if i %5 == 0:
        print(i)
    i = i + 1"""

"""soma = 0 

while soma < 50:
    num = int(input("digite um numero:"))
    soma += num
print(soma)"""

"""num = 1
c = 0 
while c < 10:
    c = c + 1
    print(f'{num} x {c} = {num*c}')
"""

qc = int(input("quantidade casais:"))

i = 0
cont = 0 
while i < qc:
    pessoa1 = input("pessoal1: ")
    pessoa2 = input("pessoal2: ")
    qfilhos = int(input(" quantidade de filhos:"))

    f = 0
    soma = 0
    maior_idade = 0
    while f < qfilhos:
        idade = int(input("idade: "))
        soma = soma + idade
        f = f + 1
        if idade > maior_idade:
            maior_idade = idade
    media = soma/qfilhos
    print("nome do casal:", pessoa1, pessoa2, "media dos idade dos filhos:", media)
    print(maior_idade)
    i = i + 1

