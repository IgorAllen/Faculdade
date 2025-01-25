livros = []

def cadastrar_livro(nome):
    """Cadastrar novo livro"""
    livros.append(nome)
    return f" Livro '{nome}' cadastrado com sucesso!"

def listar_livros():
    """Listar livros em ordem alfabética"""
    livros.sort()
    return "\n".join(f"{i+1} - {livro}" for i, livro in enumerate(livros))

def excluir_livro(numero):
    """Excluir livro pela posição"""
    if 1 <= numero <= len(livros):
        del livros[numero - 1]
        return "Livro excluído com sucesso!"
    else:
        return "O livro informado não existe!"

def alterar_livro(numero, novo_nome):
    """Alterar nome de um livro pela posição"""
    if 1 <= numero <= len(livros):
        livros[numero - 1] = novo_nome
        return "Livro alterado com sucesso!"
    else:
        return "O livro informado não existe!"