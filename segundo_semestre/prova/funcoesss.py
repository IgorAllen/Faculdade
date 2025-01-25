def menores_palavaras(frase: str):
    palavras = frase.split(" ")
    tam_menor = len(palavras[0])
    menores = []
    
    for palavra in palavras:
        if len(palavra) < tam_menor:
            tam_menor = len(palavra)

    for palavra in palavras:
        if len(palavra) == tam_menor:
            menores.append(palavra)

    return menores