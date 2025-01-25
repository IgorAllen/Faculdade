maior_peso = 0
soma_idade_macho_acima_12 = 0
gado_macho = 0
gado_femea = 0
gado_macho_acima_12 = 0
gado_zebu_m_16 = 0

raca = input('Qual a raça?  ')

while raca != 'sair':
    sexo = input('Qual o sexo do animal (M) ou (F)? ')
    idade = int(input('Qual a idade do animal? '))
    peso = float(input('Qual o peso do animal? '))
  
    if sexo == 'F' or sexo == 'f':
        gado_femea = gado_femea + 1

    if sexo == 'M' or sexo == 'm':
        gado_macho = gado_macho + 1
        if idade > 12:
            soma_idade_macho_acima_12 = soma_idade_macho_acima_12 + idade
            gado_macho_acima_12 = gado_macho_acima_12 + 1
    
    if peso > maior_peso:
        maior_peso = peso
        raca_maior_peso = raca

    if raca == 'zebu' and peso > 16:
        gado_zebu_m_16 = gado_zebu_m_16 + 1

    raca = input('Qual a raça? ')
 
idade_media_M_acima_12 = soma_idade_macho_acima_12 / gado_macho_acima_12
total_animais = gado_macho + gado_femea
perc_femea = gado_femea/total_animais

print ('O percentual de gado fêmea em relação ao gado do dia é:{}'.format(perc_femea))
print ('A idade média do gado macho acima de 12 meses de idade é: {}'.format (idade_media_M_acima_12))
print ('A raça de gado com maior peso recebido no dia foi: {}'.format(raca_maior_peso))
print ('A quantidade de gado zebu com peso maior que 16 arrobas é: {}'.format(gado_zebu_m_16))