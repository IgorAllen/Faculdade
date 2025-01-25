from notas import ler_notas, calcular_estatisticas, imprimir_resultados

notas = ler_notas()
quantidade, soma, media, acima_media, abaixo_sete = calcular_estatisticas(notas)
imprimir_resultados(notas, quantidade, soma, media, acima_media, abaixo_sete)