"""Módulo de cadastro de usuários da biblioteca."""

import re
from dataclasses import dataclass
from typing import List, Optional

REGEX_EMAIL = re.compile(r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$")


@dataclass
class Usuario:
    id: int
    nome: str
    email: str
    telefone: str

    def __str__(self) -> str:
        return f"#{self.id} {self.nome} | {self.email} | {self.telefone}"


def validar_email(email: str) -> bool:
    return bool(REGEX_EMAIL.match(email))


def normalizar_telefone(telefone: str) -> str:
    """Remove tudo que não for dígito (ex.: '(82) 99999-0000' -> '82999990000')."""
    return re.sub(r"\D", "", telefone)


def validar_telefone(telefone: str) -> bool:
    """Aceita telefones com DDD: 10 dígitos (fixo) ou 11 dígitos (celular)."""
    return len(normalizar_telefone(telefone)) in (10, 11)


class GerenciadorUsuarios:
    """Responsável pelo cadastro, consulta e remoção de usuários."""

    def __init__(self) -> None:
        self._usuarios: List[Usuario] = []
        self._proximo_id = 1

    def cadastrar(self, nome: str, email: str, telefone: str) -> Usuario:
        nome = nome.strip()
        email = email.strip().lower()

        if not nome:
            raise ValueError("O nome é obrigatório.")
        if not validar_email(email):
            raise ValueError("E-mail inválido.")
        if not validar_telefone(telefone):
            raise ValueError("Telefone inválido. Informe DDD + número (10 ou 11 dígitos).")
        if self.buscar_por_email(email):
            raise ValueError("Já existe um usuário com este e-mail.")

        usuario = Usuario(self._proximo_id, nome, email, normalizar_telefone(telefone))
        self._usuarios.append(usuario)
        self._proximo_id += 1
        return usuario

    def listar(self) -> List[Usuario]:
        return list(self._usuarios)

    def buscar_por_email(self, email: str) -> Optional[Usuario]:
        email = email.strip().lower()
        return next((u for u in self._usuarios if u.email == email), None)

    def remover(self, id_usuario: int) -> bool:
        usuario = next((u for u in self._usuarios if u.id == id_usuario), None)
        if usuario:
            self._usuarios.remove(usuario)
            return True
        return False
