def ler_notas():
    notas = []
    while True:
        nota = float(input("Digite uma nota (-1 para sair): "))
        if nota == -1:
            break
        notas.append(nota)
    return notas

def calcular_estatisticas(notas):
    quantidade = len(notas)
    soma = sum(notas)
    media = soma / quantidade
    acima_media = sum(1 for nota in notas if nota > media)
    abaixo_sete = sum(1 for nota in notas if nota < 7)
    return quantidade, soma, media, acima_media, abaixo_sete

def imprimir_resultados(notas, quantidade, soma, media, acima_media, abaixo_sete):
    print("Quantidade de notas:", quantidade)
    print("Notas:", notas)
    print("Soma:", soma)
    print("Média:", media)
    print("Notas acima da média:", acima_media)
    print("Notas abaixo de 7:", abaixo_sete)