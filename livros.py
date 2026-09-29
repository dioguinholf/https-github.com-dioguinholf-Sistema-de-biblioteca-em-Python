"""Módulo de gerenciamento e consulta de livros."""

from dataclasses import dataclass
from datetime import date
from typing import List, Optional


@dataclass
class Livro:
    isbn: str
    titulo: str
    autor: str
    ano: int

    def __str__(self) -> str:
        return f"[{self.isbn}] {self.titulo} - {self.autor} ({self.ano})"


class GerenciadorLivros:
    """Responsável por cadastrar, consultar e remover livros do acervo."""

    def __init__(self) -> None:
        self._livros: List[Livro] = []

    def adicionar(self, isbn: str, titulo: str, autor: str, ano: int) -> Livro:
        isbn, titulo, autor = isbn.strip(), titulo.strip(), autor.strip()

        if not isbn or not titulo or not autor:
            raise ValueError("ISBN, título e autor são obrigatórios.")
        if self.buscar_por_isbn(isbn):
            raise ValueError(f"Já existe um livro com o ISBN {isbn}.")
        if ano <= 0 or ano > date.today().year:
            raise ValueError("Ano de publicação inválido.")

        livro = Livro(isbn, titulo, autor, ano)
        self._livros.append(livro)
        return livro

    def listar(self) -> List[Livro]:
        return list(self._livros)

    def buscar_por_isbn(self, isbn: str) -> Optional[Livro]:
        return next((l for l in self._livros if l.isbn == isbn.strip()), None)

    def buscar_por_titulo(self, termo: str) -> List[Livro]:
        termo = termo.strip().lower()
        return [l for l in self._livros if termo in l.titulo.lower()]

    def buscar_por_autor(self, termo: str) -> List[Livro]:
        termo = termo.strip().lower()
        return [l for l in self._livros if termo in l.autor.lower()]

    def remover(self, isbn: str) -> bool:
        livro = self.buscar_por_isbn(isbn)
        if livro:
            self._livros.remove(livro)
            return True
        return False
