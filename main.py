"""Sistema de Biblioteca - ponto de entrada da aplicação."""

from livros import GerenciadorLivros
from usuarios import GerenciadorUsuarios

VERSAO = "1.0.0"

MENU = f"""
===== SISTEMA DE BIBLIOTECA v{VERSAO} =====
 LIVROS
  1 - Cadastrar livro
  2 - Listar livros
  3 - Buscar livro (título/autor/ISBN)
  4 - Remover livro
 USUÁRIOS
  5 - Cadastrar usuário
  6 - Listar usuários
  7 - Remover usuário
  0 - Sair
==========================================="""


def ler_inteiro(mensagem: str, campo: str) -> int:
    """Lê um número inteiro do teclado com mensagem de erro clara."""
    try:
        return int(input(mensagem))
    except ValueError:
        raise ValueError(f"{campo} deve ser um número inteiro.")


def exibir(itens, vazio="Nenhum registro encontrado.") -> None:
    if not itens:
        print(vazio)
    for item in itens:
        print(" ", item)


def cadastrar_livro(livros: GerenciadorLivros) -> None:
    isbn = input("ISBN: ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = ler_inteiro("Ano: ", "O ano")
    livro = livros.adicionar(isbn, titulo, autor, ano)
    print("Livro cadastrado:", livro)


def buscar_livro(livros: GerenciadorLivros) -> None:
    tipo = input("Buscar por (t)ítulo, (a)utor ou (i)SBN? ").strip().lower()
    termo = input("Termo de busca: ")
    if tipo == "t":
        exibir(livros.buscar_por_titulo(termo))
    elif tipo == "a":
        exibir(livros.buscar_por_autor(termo))
    elif tipo == "i":
        livro = livros.buscar_por_isbn(termo)
        exibir([livro] if livro else [])
    else:
        print("Opção de busca inválida.")


def cadastrar_usuario(usuarios: GerenciadorUsuarios) -> None:
    nome = input("Nome: ")
    email = input("E-mail: ")
    telefone = input("Telefone (com DDD): ")
    usuario = usuarios.cadastrar(nome, email, telefone)
    print("Usuário cadastrado:", usuario)


def main() -> None:
    livros = GerenciadorLivros()
    usuarios = GerenciadorUsuarios()

    while True:
        print(MENU)
        opcao = input("Escolha uma opção: ").strip()
        try:
            if opcao == "1":
                cadastrar_livro(livros)
            elif opcao == "2":
                exibir(livros.listar(), "Acervo vazio.")
            elif opcao == "3":
                buscar_livro(livros)
            elif opcao == "4":
                ok = livros.remover(input("ISBN do livro: "))
                print("Livro removido." if ok else "Livro não encontrado.")
            elif opcao == "5":
                cadastrar_usuario(usuarios)
            elif opcao == "6":
                exibir(usuarios.listar(), "Nenhum usuário cadastrado.")
            elif opcao == "7":
                ok = usuarios.remover(ler_inteiro("ID do usuário: ", "O ID"))
                print("Usuário removido." if ok else "Usuário não encontrado.")
            elif opcao == "0":
                print("Até logo!")
                break
            else:
                print("Opção inválida.")
        except ValueError as erro:
            print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
