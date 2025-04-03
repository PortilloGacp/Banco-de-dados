# Banco de Dados - Cadastro para Time da Faculdade

Este projeto consiste em um sistema de cadastro desenvolvido para auxiliar na organização de times da faculdade. Através de uma interface web intuitiva, os usuários podem inserir seus dados, facilitando a formação de equipes para diversas atividades e competições.

## Funcionalidades

* Cadastro de usuários com informações relevantes.
* Armazenamento e gerenciamento dos dados cadastrados em um banco de dados.
* Interface web responsiva e de fácil navegação.
* Possibilidade de futura implementação de funcionalidades como busca por usuários e formação de times automáticos.

## Tecnologias Utilizadas

* **Linguagem de programação:** Python
* **Framework:** Django
* **Front-end:** HTML, CSS

## Instalação

1.  Clone o repositório: `git clone https://github.com/seu-usuario/banco-de-dados.git`
2.  Crie um ambiente virtual (recomendado):
    * `python -m venv venv`
    * `source venv/bin/activate` (Linux/macOS) ou `venv\Scripts\activate` (Windows)
3.  Instale as dependências: `pip install -r requirements.txt`
4.  Realize as migrações do banco de dados: `python manage.py migrate`
5.  Crie um superusuário para acessar o painel administrativo (opcional): `python manage.py createsuperuser`

## Execução

1.  Execute o servidor de desenvolvimento: `python manage.py runserver`
2.  Acesse a aplicação no seu navegador: `http://127.0.0.1:8000/`


## Agradecimentos

* Agradecimentos à comunidade Django por fornecer uma ferramenta tão poderosa e flexível.
* Agradecimentos a todos que contribuíram para este projeto.
