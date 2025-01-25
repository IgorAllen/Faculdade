from saltos import calcular_media_saltos, imprimir_resultados

nome = input("Digite o nome do atleta: ")
saltos = []
for i in range(5):
    salto = float(input(f"Digite o {i+1}º salto: "))
    saltos.append(salto)
media = calcular_media_saltos(saltos)
imprimir_resultados(nome, saltos, media)