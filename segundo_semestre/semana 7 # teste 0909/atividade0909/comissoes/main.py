from comissoes import calcular_comissao, classificar_comissoes

vendas = [3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
comissoes = [calcular_comissao(venda) for venda in vendas]
classificacao = classificar_comissoes(comissoes)
print("Classificação de comissões:")
for faixa, quantidade in classificacao.items():
    print(f"{faixa}: {quantidade}")