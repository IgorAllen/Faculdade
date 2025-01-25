def calcular_percentual(votos, total_votos):
    return (votos / total_votos) * 100

def imprimir_resultados(votos, total_votos):
    print("Resultado da votação:")
    print(f"Foram computados {total_votos} votos.")
    for jogador, votos in votos.items():
        percentual = calcular_percentual(votos, total_votos)
        print(f"Jogador {jogador}: {votos} votos ({percentual:.2f}%)")
    melhor_jogador = max(votos, key=votos.get)
    print(f"O melhor jogador foi o número {melhor_jogador}, com {votos[melhor_jogador]} votos, correspondendo a {calcular_percentual(votos[melhor_jogador], total_votos):.2f}% do total de votos.")