def imprimePares(lista):
    
    pares=[]
    for numero in lista:
        if numero %2 == 0:
            pares.append(numero)
    
    return pares


def estaContido(string1:str, string2):
    verificar=string1.find(string2)
    if verificar != -1:
        return True
    else:
        return False


def criaPalavra(*palavras):

    nova_palavra = ''.join(palavra[0] for palavra in palavras if palavra)
    return(nova_palavra)
