# 📚 Sistema de Biblioteca

## Nome
**Sistema de Biblioteca**: aplicação de linha de comando em Python para gerenciamento de acervo e usuários.

## Objetivo
Desenvolver um sistema simples e modularizado para cadastro e consulta de livros e usuários. Ele serve como base prática para a atividade de **Gerência de Configuração e Controle de Versão**, cobrindo commits semânticos, versionamento com tags e evolução incremental do código com Git.

## Principais Funcionalidades
- **Gerenciamento de livros** (`livros.py`)
  - Cadastro de livros (ISBN, título, autor e ano)
  - Listagem do acervo
  - Consulta por título, autor ou ISBN
  - Remoção de livros
- **Cadastro de usuários** (`usuarios.py`)
  - Cadastro com nome, e-mail e telefone
  - Validação de e-mail e telefone
  - Bloqueio de e-mails duplicados
  - Listagem e remoção de usuários
- **Menu interativo** (`main.py`) que integra todos os módulos

## Estrutura do Projeto
```
sistema-biblioteca/
├── README.md
├── .gitignore
├── livros.py
├── usuarios.py
└── main.py
```

## Como Executar
Requisito: Python 3.8 ou superior.

```bash
python main.py
```

## Versionamento
O projeto segue o [Versionamento Semântico](https://semver.org/lang/pt-BR/) (`MAJOR.MINOR.PATCH`).

| Versão | Descrição |
|--------|-----------|
| v1.0.0 | Módulos de livros e usuários integrados |
| v1.1.0 | Validação do ano de publicação (não aceita anos futuros) |

## Integrantes
| Nome | GitHub |
|------|--------|
| Diogo | @dioguinholf |
