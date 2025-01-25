def adicionar_item(lista_de_compras, nome_produto, quantidade):
    lista_de_compras[nome_produto] = quantidade


def exibir_lista_completa(lista_de_compras: dict):
    cont = 1
    for nome_produto, quantidade in lista_de_compras.items():
        print(f"{cont} - Item: {nome_produto} | Qtde: {quantidade}")
        cont += 1

def atualizar_quantidade_item(lista_de_compras, nome_produto, quantidade):
    lista_de_compras[nome_produto] = quantidade


def remover_item(lista_de_compras: dict, nome_produto):
    lista_de_compras.pop(nome_produto)