# Estudo Django API

API Django de estudo com autenticação JWT e gestão de livros.

## Visão geral

O projeto tem dois apps principais:

- `custom_auth`: registro de usuários, login, geração de token JWT, refresh e gerenciamento de usuários
- `livros`: gerenciamento de livros associados ao usuário autenticado

## Tecnologias

- Python
- Django
- Django REST Framework
- Django REST Framework SimpleJWT
- drf-yasg (Swagger / Redoc)

## Instalação

```bash
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

> Se ainda não existir, crie um `requirements.txt` com as dependências do projeto.

## URLs principais

- `http://localhost:8000/swagger/` - documentação Swagger UI
- `http://localhost:8000/redoc/` - documentação Redoc
- `http://localhost:8000/auth/register/` - registrar usuário
- `http://localhost:8000/auth/login/` - login e retorno de `access` + `refresh`
- `http://localhost:8000/auth/refresh/` - renovar token JWT
- `http://localhost:8000/auth/users/` - listar usuários (somente superuser)
- `http://localhost:8000/auth/users/<id>/` - ver, atualizar ou deletar usuário próprio ou para superuser
- `http://localhost:8000/auth/superusers/` - criar superusuário (somente superuser)
- `http://localhost:8000/livros/` - CRUD de livros do usuário autenticado

## Autenticação

A API usa JWT. Para acessar rotas protegidas, envie o header:

```http
Authorization: Bearer <access_token>
```

No Swagger, use o botão `Authorize` e insira o token com o prefixo `Bearer `.

## Endpoints de exemplo

### Registrar usuário

`POST /auth/register/`

Corpo JSON:

```json
{
  "username": "usuario1",
  "email": "usuario1@example.com",
  "password": "senha123"
}
```

### Login

`POST /auth/login/`

Corpo JSON:

```json
{
  "username": "usuario1",
  "password": "senha123"
}
```

Resposta esperada:

```json
{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}
```

### Criar livro

`POST /livros/`

Header:

```http
Authorization: Bearer <access_token>
```

Corpo JSON:

```json
{
  "titulo": "Meu Livro",
  "autor": "Autor Exemplo",
  "publicado_em": "2026-04-13",
  "status": "nao lido"
}
```

### Listar livros do usuário

`GET /livros/`

Header:

```http
Authorization: Bearer <access_token>
```

## Estrutura do projeto

- `setup/` - projeto Django
- `custom_auth/` - app de autenticação e usuários
- `livros/` - app de gerenciamento de livros
- `manage.py` - comando de gerenciamento Django
- `.gitignore` - arquivos ignorados pelo Git
