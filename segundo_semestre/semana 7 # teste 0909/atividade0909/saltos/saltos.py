def calcular_media_saltos(saltos):
    return sum(saltos) / len(saltos)

def imprimir_resultados(nome, saltos, media):
    print(f"Atleta: {nome}")
    print("Saltos:")
    for i, salto in enumerate(saltos):
        print(f"{i+1}º Salto: {salto} m")
    print(f"Média dos saltos: {media} m")