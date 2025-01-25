def contarObjetos(lista):
    contarobjetos={}
    
    for objeto in lista:
        if objeto in contarobjetos:
            contarobjetos[objeto]+=1
        else:
            contarobjetos[objeto]=1

    return contarobjetos

