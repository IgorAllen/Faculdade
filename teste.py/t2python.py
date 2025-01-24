"""
tabela_dados = [['Ana', 23,'São Paulo'],
                ['Jose', 25, 'Palmas'],
                ['Maria', 32, 'Aracaju']]

i = 0 
while i < len(tabela_dados):
    print(tabela_dados[i][2])
    i = i + 1

tabela_dados.append(['Evelin', 12, 'Goiania'])
print(tabela_dados)

nome = input ('Digite o nome: ')
while nome != 'sair':
    cliente = []
    idade = int(input)('Digite a idade: ')
    cidade = input("Digite a cidade: ")
    cliente.append(nome)
    cliente.append(idade)
    cliente.append(cidade)
    tabela_dados.append(cliente)
    nome = input('Digite o nome')
    print(tabela_dados)"""


print("======================================================")

"""alunos = [[aluno,nota_g1, nota_g2],
 [aluno, nota_g1, nota_g2]] """
alunos = []
deseja_continuar = 's'
while deseja_continuar != 'n':
    cada_aluno = []
    aluno = input('Degite o nome do aluno: ')
    nota_g1 = int(input('Digite a G1:'))
    nota_g2 = int(input('Digite a G2:'))
    cada_aluno.append(aluno)
    cada_aluno.append(nota_g1)
    cada_aluno.append(nota_g2)
    alunos.append(cada_aluno)
    deseja_continuar = input('Deseja Continuar? ')
print(alunos)

i = 0
while i < len(alunos):
    media = (alunos[i][1]+alunos[i][2]*2)/3
    print ('A MEDIA DO ALUO () É ()'.format(alunos[i][0], media))
    i = i + 1

ele não volta e testa outras opções.

