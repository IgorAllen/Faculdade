def calcular_comissao(vendas):
    comissao = 200 + (vendas * 0.09)
    return comissao

def classificar_comissoes(comissoes):
    classificacao = {
        "200-299": 0,
        "300-399": 0,
        "400-499": 0,
        "500-599": 0,
        "600-699": 0,
        "700-799": 0,
        "800-899": 0,
        "900-999": 0,
        "1000+": 0
    }
    for comissao in comissoes:
        if comissao >= 200 and comissao < 300:
            classificacao["200-299"] += 1
        elif comissao >= 300 and comissao < 400:
            classificacao["300-399"] += 1
        elif comissao >= 400 and comissao < 500:
            classificacao["400-499"] += 1
        elif comissao >= 500 and comissao < 600:
            classificacao["500-599"] += 1
        elif comissao >= 600 and comissao < 700:
            classificacao["600-699"] += 1
        elif comissao >= 700 and comissao < 800:
            classificacao["700-799"] += 1
        elif comissao >= 800 and comissao < 900:
            classificacao["800-899"] += 1
        elif comissao >= 900 and comissao < 1000:
            classificacao["900-999"] += 1
        else:
            classificacao["1000+"] += 1
    return classificacao