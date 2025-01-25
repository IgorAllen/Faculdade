# def soma_notas(notas):
#     soma = 0
#     for nota in notas:
#         soma += nota
#     return soma

def calcula_media(notas):
    # media = soma_notas(notas)/len(notas)
    media = sum(notas)/len(notas)
    return media

def calcula_situacao(media_aluno, media_necessaria):
    if media_aluno >= media_necessaria:
        return "Aprovado!"
    else:
        return "Reprovado!"