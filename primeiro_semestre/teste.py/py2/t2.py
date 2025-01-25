#Programa que monta lista de alunos:

listaAlunos = []

continuar = 's'

while continuar == 's':
    nomeAluno = input('Digite o nome dos alunos:')
    listaAlunos.append(nomeAluno)
    continuar = input('Deseja continuar [s ou n]:')
print(listaAlunos)

#Quantidade de elementos em uma lista:

print('Qt. de elementos:',len(listaAlunos))
i = 0

while i < len(listaAlunos):
    print(listaAlunos[i])
    i = i+1

#Como pedir se tem algo/aluno na lista:

nomeparaBusca = input('Digite um nome para buscar:')

if nomeparaBusca in listaAlunos:
    print('existe alunos')
else:
    print('Não existe alunos!!!')

