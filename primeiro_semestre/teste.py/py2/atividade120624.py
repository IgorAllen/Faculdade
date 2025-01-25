
alcool = float(input("Digite o preço do alcool: "))
diesel = float(input("Digite o preço do diesel: "))
gasolina = float(input("Digite o preço do gasolina: "))

categoria = input("Digite a categoria do produto 'alcool', 'diesel', 'gasolina': ")
while categoria != "sair":
    litros = float(input("Digite a quantidade: "))
    pagameneto = input("Digite a forma de pagamento: ")
    if pagameneto == "pix" and categoria == 'gasolina':
        valor_pix = (litros * gasolina) * 0.03
        print("O valor a pagar será: ",valor_pix)
    elif pagameneto == "pix" and categoria == 'diesel':
        valor_pix = (litros * diesel) * 0.03
        print("O valor a pagar será: ",valor_pix)
    elif pagameneto == "pix" and categoria  == 'alcool':
        valor_pix = (litros * alcool) * 0.03
        print("O valor a pagar será: ",valor_pix)
    else:
        print('Não existe essa categoria ou essa forma de pagamento')
        if pagameneto == "dinheiro" and categoria == 'gasolina':
            valor_dinheiro = (litros * gasolina)*0.05
            print("O valor a pagar será: ",valor_dinheiro)
        elif pagameneto == "dinheiro" and categoria == 'diesel':
            valor_dinheiro = (litros * diesel)*0.05
            print("O valor a pagar será: ",valor_dinheiro)
        elif pagameneto == "dinheiro" and categoria == 'alcool':
            valor_dinheiro = (litros * alcool)*0.03
            print("O valor a pagar será: ",valor_dinheiro)
        else:
            print('Não existe essa categoria ou essa forma de pagamento')
        categoria = input("Digite a categoria do produto: ")
"""
    if valor_dinheiro == 0:
    valor_sem_desconto = valor_dinheiro /0,03
    print('O valor sem desconta é: ',valor_sem_desconto)
    if valor_pix == 0 and :
    valor_sem_desconto = valor_pix /0,05
    print('O valor sem desconta é: ',valor_sem_desconto)
"""        
"""       
print('O valor sem desconto do pix é', valor_pix/0,03)
print('O valor sem desconto do dinheiro é', valor_dinheiro/0,05)
"""       