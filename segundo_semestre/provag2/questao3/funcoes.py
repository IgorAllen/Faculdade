def verificarSituacao(lista:list):
    lista2=[]

    for aluno in lista:
        if aluno["percentual"] >=75:   

            if aluno["notaG1"] >=6:
                if aluno["notaG2"] >=6:
                    lista2.append({
                        "situação":"aprovado"
                        })
                elif aluno["notaG1"]<6:
                    lista2.append({
                         "situação":"recuperação"
                    })

            elif aluno["notaG1"] <6.0:
                if aluno["notaG2"] >=6.0:
                    lista2.append({
                         "situação":"recuperação"
                    })
        else:
            lista.append({
                 "situação":"reprovado"
            })
    
    return lista2
    
            