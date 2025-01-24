pesomaximo = int(input("Peso máximo permitido:"))
veiculos = 0
veiculosmultados = 0
totalmultas = 0
while veiculos < 60:
    placadoveiculo = input('Qual é a placa do veiculo?')
    pesoveiculo = int(input('Qual é o peso do veiculo?'))
    veiculos = veiculos + 1

    if pesoveiculo <= pesomaximo:
        print("Peso dentro do limite permitido!")
    else:
        print("Peso ultrapassou o limite permitido!")
        print('A placa do veiculo é: ',placadoveiculo)
    
        multa = (pesoveiculo - pesomaximo)*15
        print("Você terar que pagar a multa com o valor de ", multa, " reais")
        veiculosmultados = veiculosmultados + 1
        totalmultas = totalmultas + multa

print("A quantidade de veiculos multados é de:",veiculosmultados/veiculos)
print("O total de multas é de:",totalmultas)

