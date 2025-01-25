
import funcoes

alunos = []
media_necessaria = 7
qtde_aprovados = 0
qtde_reprovados = 0

while True:
    nome_aluno = input("Entre com o nome do aluno (ou 'sair' para encerrar): ")
    if nome_aluno == "sair":
        break
    
    nota1 = float(input("Entre com a nota do 1º bimestre: "))
    nota2 = float(input("Entre com a nota do 2º bimestre: "))
    nota3 = float(input("Entre com a nota do 3º bimestre: "))
    nota4 = float(input("Entre com a nota do 4º bimestre: "))

    alunos.append([nome_aluno, [nota1, nota2, nota3, nota4]])


for nome, notas in alunos:
    media = funcoes.calcula_media(notas)
    situacao = funcoes.calcula_situacao(media, media_necessaria)

    print(f"{nome} - {situacao}")

    if media >= media_necessaria:
        qtde_aprovados += 1
    else:
        qtde_reprovados += 1

print("Total de alunos")
print(f"\tAprovados: {qtde_aprovados}")
print(f"\tReprovados: {qtde_reprovados}")
