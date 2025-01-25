import no1
organizacao=[]
notas=[]
notasgerais=[]
i=0
media=0
reprovacoes=0
aprovacoes=0

while True:
    nome=(input('Digite o nome do(a) aluno(a): '))
    if nome == 'sair':
        break
    nota1=float(input('Digite a nota do 1 bimestre: '))
    nota2=float(input('Digite a nota do 2 bimestre: '))
    nota3=float(input('Digite a nota do 3 bimestre: '))
    nota4=float(input('Digite a nota do 4 bimestre: '))
    nomeL=[nome]
    notas=[nota1,nota2,nota3,nota4]
    notasgerais.append(notas)
    organizacao.append(nomeL)
    
while i< len(organizacao):
    media=no1.calculomedia(notasgerais[i])
    if media<7:
        organizacao[i].append('- Reprovado(a)')
        reprovacoes+=1
    else :
        organizacao[i].append('- Aprovado(a)')
        aprovacoes+=1
    i+=1
print(organizacao)
print('Aprovações ',aprovacoes)
print('Reprovações ',reprovacoes)
