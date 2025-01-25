def calcular_preco_final(preco_inicial, tipo_cliente):
    if tipo_cliente == "VIP":
        desconto = 0.3
    elif tipo_cliente == "Frequentador":
        if preco_inicial >= 500:
            desconto = 0.2
        elif preco_inicial >= 200:
            desconto = 0.1
        else:
            desconto = 0.05
    else:
        desconto = 0.0
    preco_final = preco_inicial * (1 - desconto)
    if preco_final > 1000:
        preco_final -= 50  # Desconto adicional
    return preco_final
