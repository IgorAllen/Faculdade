def soma_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    nnn1 = cpf[:3]
    nnn2 = cpf[3:6]
    nnn3 = cpf[6:9]
    nn = cpf[9:11]
    soma = int(nnn1) + int(nnn2) + int(nnn3) + int(nn)
    return soma


def ultima_palavra_junior(frase):
    ultima = frase.split()[-1]
    return ultima in ['Junior', 'Filho', 'Neto', 'Sobrinho']

def duas_ultimas_palavras(frase):
    palavras = frase.split()
    return ' '.join(palavras[-2:])

def ultima_palavra(frase):
    palavras = frase.split()
    return palavras[-1]

def palavras_sem_duas_ultimas(frase):
    palavras = frase.split()
    return palavras[:-2]

def palavras_sem_ultima(frase):
    palavras = frase.split()
    return palavras[:-1]

def primeira_letra_lista(palavras):
    return '. '.join([palavra[0] for palavra in palavras]) + '.'

def palavra_especial(palavra):
    return palavra in ['da', 'de', 'das', 'do', 'dos', 'e']

def primeira_letra_lista_especial(palavras):
    resultado = []
    for palavra in palavras:
        if palavra_especial(palavra):
            resultado.append(palavra)
        else:
            resultado.append(palavra[0])
    return '. '.join(resultado) + '.'

def frase_maiusculas(frase):
    return frase.upper()

def concatenar_frases(frase1, frase2):
    return f"{frase1}, {frase2}"