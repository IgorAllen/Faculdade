from funcoes import *

arquivo=open("questao3/notas.txt","r")

dadosAlunos = arquivo.read().strip().splitlines()
arquivo.close()

Alunos = []

for dados in dadosAlunos:
    nome,notaG1,notaG2,percentual = dados.split(",")
    notaG1,notaG2,percentual=float(notaG1),float(notaG2),float(percentual)
    Alunos.append({
        "nome":nome,
        "notaG1":notaG1,
        "notaG2":notaG2,
        "percentual":percentual,
        })
    
print(Alunos)

(resultado)=verificarSituacao(Alunos)

arquivo=open("questao3/notas.txt","w")
for i in range (len(Alunos)):
    nome=Alunos["nome"]
    notaG1=Alunos["notaG1"]
    notaG2=Alunos["notaG2"]
    percentual=Alunos["percentual"]
    arquivo.write(f"{nome} , {notaG2} , {notaG2} , {percentual} , {resultado[i]}\n")
arquivo.close()

