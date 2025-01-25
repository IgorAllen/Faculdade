def calcular_percentual(votos, total_votos):
    return (votos / total_votos) * 100

def imprimir_resultados(votos, total_votos):
    print("Resultado da enquete:")
    print(f"Foram computados {total_votos} votos.")
    for sistema, votos in votos.items():
        percentual = calcular_percentual(votos, total_votos)
        print(f"{sistema}: {votos} votos ({percentual:.2f}%)")
    melhor_sistema = max(votos, key=votos.get)
    print(f"O sistema operacional mais votado foi o {melhor_sistema}, com {votos[melhor_sistema]} votos, correspondendo a {calcular_percentual(votos[melhor_sistema], total_votos):.2f}% do total de votos.")