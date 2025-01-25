"""
Faça o programa abaixo funcionar, para isso, implemente o módulo
com as funções correspondentes.
Obs.: os parâmetros das funções não devem ser alterados!
"""


from funcoes import *

# Produto / Quantidade
lista_de_compras = {"arroz": 2, "refrigerante": 10}

while True:
    print("-" * 30 + "MENU" + 30 * "-")
    menu = input(        
        "[1] - Adicionar item à lista\n"
        "[2] - Exibir a lista completa\n"
        "[3] - Atualizar quantidade de um item\n"
        "[4] - Remover item à lista\n"
        "[0] - Sair\n"
        "-> "
    )

    if menu == "1":
        # 0,25
        nome_produto = input("Nome do produto: ").lower()
        quantidade = int(input("Quantidade: "))
        
        adicionar_item(lista_de_compras, nome_produto, quantidade)
    elif menu == "2":
        # 0,25
        exibir_lista_completa(lista_de_compras)
        """
        Exemplo de saída:
        1 - Item: Arroz | Qtde: 2
        2 - Item: Refrigerante | Qtde: 10
        ...
        """        
    elif menu == "3":
        # 0,25
        exibir_lista_completa(lista_de_compras)
        nome_produto = input("Nome do produto: ").lower()
        quantidade = int(input("Quantidade: "))

        atualizar_quantidade_item(lista_de_compras, nome_produto, quantidade)
    elif menu == "4":                
        # 0,25
        exibir_lista_completa(lista_de_compras)
        nome_produto = input("Nome do produto: ").lower()

        remover_item(lista_de_compras, nome_produto)
    elif menu == "0":
        break
    else:
        print("Opção inválida!")