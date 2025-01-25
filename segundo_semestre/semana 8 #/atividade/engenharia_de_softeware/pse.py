import es

def main():
    preco_inicial = float(input("Digite o preço inicial: "))
    tipo_cliente = input("Digite o tipo de cliente (VIP, Frequentador ou outro): ")

    preco_final = es.calcular_preco_final(preco_inicial, tipo_cliente)

    print(f"O preço final é: R$ {preco_final:.2f}")

if __name__ == "__main__":
    main()
