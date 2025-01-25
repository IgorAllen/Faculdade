from funcao import *

# (1) Questão

cpf = input("Digite um CPF no formato nnn.nnn.nnn-nn: ")
print("Soma do CPF:", soma_cpf(cpf))

# (2) Questão

frase = input("Digite uma frase: ")
print("Última palavra é Junior, Filho, Neto ou Sobrinho?", ultima_palavra_junior(frase))

# (3) Questão

print("Duas últimas palavras:", duas_ultimas_palavras(frase))

# (4) Questão

print("Última palavra:", ultima_palavra(frase))

# (5) Questão

print("Palavras sem as duas últimas:", palavras_sem_duas_ultimas(frase))

# (6) Questão

print("Palavras sem a última:", palavras_sem_ultima(frase))

# (7) Questão

lista_palavras = input("Digite uma lista de palavras separadas por espaço: ").split()
print("Primeira letra de cada palavra:", primeira_letra_lista(lista_palavras))

# (8) Questão

palavra = input("Digite uma palavra: ")
print("A palavra é especial?", palavra_especial(palavra))

# (9) Questão

print("Primeira letra com palavras especiais:", primeira_letra_lista_especial(lista_palavras))

# (10) Questão

print("Frase em maiúsculas:", frase_maiusculas(frase))

# (11) Questão

frase2 = input("Digite outra frase: ")
print("Frases concatenadas:", concatenar_frases(frase, frase2))