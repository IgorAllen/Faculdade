from enquete import imprimir_resultados

votos = {
    "Windows Server": 0,
    "Unix": 0,
    "Linux": 0,
    "Netware": 0,
    "Mac OS": 0,
    "Outro": 0
}
while True:
    sistema = int(input("Digite o número do sistema operacional (0 para sair): "))
    if sistema == 0:
        break
    if sistema == 1:
        votos["Windows Server"] += 1
    elif sistema == 2:
        votos["Unix"] += 1
    elif sistema == 3:
        votos["Linux"] += 1
    elif sistema == 4:
        votos["Netware"] += 1
    elif sistema == 5:
        votos["Mac OS"] += 1
    elif sistema == 6:
        votos["Outro"] += 1
    else:
        print("Opção inválida. Tente novamente.")
imprimir_resultados(votos, sum(votos.values()))