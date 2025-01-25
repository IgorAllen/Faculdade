arquivo = open("alunos.txt", "r")
dadosAlunos = arquivo.read().strip().splitlines()
arquivo.close()

alunos = []

dadosAlunos.pop(0)
for dados in dadosAlunos:
    nome, g1, g2 = dados.split(",")
    g1, g2 = float(g1), float(g2)
    media = (g1 + (g2 * 2))/3
    alunos.append({
        "nome": nome,
        "g1": g1,
        "g2": g2,
        "media": round(media, 2) #round(media, numero de casas) -> arredonda a média para numero de casas decimais
})

arquivo = open("medias.txt", "w") # "w" ele cria um a arquivo se não existir;
arquivo.write("nome, media\n")
for aluno in alunos:
    arquivo.write(f"{aluno['nome']}, {aluno['media']}\n") # Eu estou concatenando strings e variáveis
arquivo.close()

