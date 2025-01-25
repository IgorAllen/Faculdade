

produtos = [['031','iphone',5000, 12],
            ['046','ipad',1300, 15]]

codigo = input('Digite o código: ')

while codigo != '0':
    novo_produto = []
    novo_produto.append(codigo)
    produtos = input('Digite o produto:')
    novo_produto.append(produtos)
    preco = float(input('Digite o preço:'))
    novo_produto.append(preco)
    estoque = int(input("Digite a qtde do produto: "))
    novo_produto.append(estoque)
    produtos.append(novo_produto)
    codigo = input('Digite o código: ')
    
    i = 0 
    while i < len(produtos):
        print(produtos[i][0], produtos[i][1], produtos[i][2], produtos[i][3])
        i = i + 1

    i = 0
    while i < len(produtos):
        if produtos[i][2]>2200:
            print('Esse produto tem preço > 2200:', produtos[i][1])
        if produtos [i][3]<20:
            print('Codigo do produto < 20:', produtos[i][3])
        i = i + 1
