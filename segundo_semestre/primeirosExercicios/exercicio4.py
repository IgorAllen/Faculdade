
def desconto():
    
    valor_produto = float(input("Digite o valor do produto: "))
    valor_com_desconto = valor_produto * 0.9
    print("O valor do produto com desconto é:", valor_com_desconto)
    return valor_com_desconto

desconto()
