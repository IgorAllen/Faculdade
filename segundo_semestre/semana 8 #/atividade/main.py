import livraria

def main():
    while True:
        print("\nMenu:")
        print("[1] Registrar livros")
        print("[2] Listar livros")
        print("[3] Excluir livro")
        print("[4] Alterar livro")
        print("[5] Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Informe o nome do livro: ")
            print(livraria.cadastrar_livro(nome))
        elif opcao == "2":
            print(livraria.listar_livros())
        elif opcao == "3":
            numero = int(input("Informe o número do livro a ser excluído: "))
            print(livraria.excluir_livro(numero))
        elif opcao == "4":
            numero = int(input("Informe o número do livro a ser alterado: "))
            novo_nome = input("Informe o novo nome do livro: ")
            print(livraria.alterar_livro(numero, novo_nome))
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente!")

























if __name__ == "__main__":
    main()













#sem input dentro de uma função.
