gabarito = ['a','c','d','a','c','a']
resposta = []
acertos = 0
i = 0
while i < len(gabarito):
    resp = input('Digite a resposta: ')
    resposta.append(resp)
    i = i + 1
print(gabarito)
print(resposta)

i = 0
while i < 6:
    if gabarito[i] == resposta[i]:
        acertos = acertos + 1
    i = i + 1

if acertos >= 3:
    print("Aluno Aprovado")
    print("O percentual de acertos é ",acertos/len(gabarito))
else:
    print("Aluno Reprovado")
