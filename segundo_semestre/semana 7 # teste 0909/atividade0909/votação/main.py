from votacao import imprimir_resultados

votos = {}
while True:
    jogador = int(input("Número do jogador (0 para sair): "))
    if jogador == 0:
        break
    if jogador not in votos:
        votos[jogador] = 0
    votos[jogador] += 1
imprimir_resultados(votos, sum(votos.values()))