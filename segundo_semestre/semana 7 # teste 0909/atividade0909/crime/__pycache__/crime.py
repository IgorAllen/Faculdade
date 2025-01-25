def perguntas():
    perguntas = [
        "Telefonou para a vítima?",
        "Esteve no local do crime?",
        "Mora perto da vítima?",
        "Devia para a vítima?",
        "Já trabalhou com a vítima?"
    ]
    respostas = []
    for pergunta in perguntas:
        resposta = input(pergunta + " (s/n): ")
        respostas.append(resposta.lower() == "s")
    return respostas

def classificar(respostas):
    contagem = sum(respostas)
    if contagem == 2:
        return "Suspeita"
    elif contagem >= 3 and contagem <= 4:
        return "Cúmplice"
    elif contagem == 5:
        return "Assassino"
    else:
        return "Inocente"