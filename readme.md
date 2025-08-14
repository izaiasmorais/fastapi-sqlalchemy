# FastAPI Clean

## Introdução

Uma API auto-documentável com FastAPI, Pydantic e SQLAlchemy.

## Tecnologias

- Linguagem: [Python](https://www.python.org)
- Framework: [FastAPI](https://fastapi.tiangolo.com)
- ORM: [SQLAlchemy](https://sqlalchemy.org) (Async)
- Documentação: [Swagger](https://swagger.io/) (automática via FastAPI)
- Banco de Dados: [PostgreSQL](https://www.postgresql.org)
- Autenticação: [JWT](https://jwt.io)
- Gerenciamento de Dependências: [uv](https://docs.astral.sh/uv/)
- Validação: [Pydantic](https://pydantic.dev)
- Migrations: [Alembic](https://alembic.sqlalchemy.org/)
- Hash de Senhas: [Passlib](https://passlib.readthedocs.io)

## Estrutura do Projeto

| Diretório/Arquivo              | Descrição                                             |
| ------------------------------ | ----------------------------------------------------- |
| **alembic/**                   | Migrações do banco de dados (Alembic)                 |
| **src/**                       | Código-fonte principal da aplicação                   |
| └─ **controllers/**            | Controladores para lidar com requisições HTTP         |
| &nbsp;&nbsp;&nbsp;└─ **auth/** | Endpoints de autenticação (sign-up, sign-in, profile) |
| └─ **models/**                 | Modelos do banco de dados (SQLAlchemy)                |
| └─ **schemas/**                | Esquemas de validação de dados (Pydantic)             |
| └─ **utils/**                  | Funções utilitárias e helpers                         |
| └─ **main.py**                 | Configuração principal da aplicação FastAPI           |
| └─ **database.py**             | Configurações do banco de dados e SQLAlchemy          |
| **docker-compose.yml**         | Configuração do PostgreSQL via Docker                 |
| **pyproject.toml**             | Dependências e configurações do projeto               |
| **alembic.ini**                | Configuração do Alembic para migrações                |
| **Makefile**                   | Comandos úteis para desenvolvimento                   |

## Endpoints

| Método   | Endpoint        | Descrição                                   | Autenticação |
| -------- | --------------- | ------------------------------------------- | ------------ |
| **GET**  | `/health`       | Health check da API                         | ❌           |
| **POST** | `/auth/sign-up` | Registrar um novo usuário                   | ❌           |
| **POST** | `/auth/sign-in` | Fazer login e obter o token de autenticação | ❌           |
| **GET**  | `/auth/profile` | Obter o perfil do usuário autenticado       | ✅           |

## Instalação

Clone o repositório na sua máquina:

```bash
git clone https://github.com/izaiasmorais/fastapi-clean
```

Acesse o projeto:

```bash
cd fastapi-clean
```

Instale o UV (se ainda não tiver):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Crie e ative o ambiente virtual:

```bash
uv venv
source .venv/bin/activate
```

Instale as dependências:

```bash
uv sync
```

## Executando o Projeto

Rode o banco PostgreSQL no Docker:

```bash
docker compose up -d
```

Configure as variáveis de ambiente (crie um arquivo `.env` baseando-se nas variáveis usadas no código):

```env
SECRET_KEY="seu-secret-key-super-seguro"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL="postgresql://postgres:postgres123@localhost:5432/fastapi_auth"
```

Crie a primeira migração (apenas na primeira vez):

```bash
DATABASE_URL="postgresql://postgres:postgres123@localhost:5432/fastapi_auth" uv run alembic revision --autogenerate -m "Initial migration"
```

Aplique a migração:

```bash
DATABASE_URL="postgresql://postgres:postgres123@localhost:5432/fastapi_auth" uv run alembic upgrade head
```

Para migrações futuras, use:

```bash
DATABASE_URL="postgresql://postgres:postgres123@localhost:5432/fastapi_auth" uv run alembic revision --autogenerate -m "Sua mensagem"
DATABASE_URL="postgresql://postgres:postgres123@localhost:5432/fastapi_auth" uv run alembic upgrade head
```

Inicie o servidor de desenvolvimento:

```bash
make dev
```

Ou manualmente:

```bash
uv run python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

A API estará disponível em: http://localhost:8000

A documentação Swagger estará em: http://localhost:8000 (configurado como página inicial)

## Comandos Úteis

### Desenvolvimento

```bash
# Servidor de desenvolvimento com reload automático
make dev

# Servidor de produção
make start
```

### Migrações

```bash
# Criar nova migração após mudanças nos modelos
DATABASE_URL="postgresql://postgres:postgres123@localhost:5432/fastapi_auth" uv run alembic revision --autogenerate -m "Sua mensagem"

# Aplicar migrações
DATABASE_URL="postgresql://postgres:postgres123@localhost:5432/fastapi_auth" uv run alembic upgrade head

# Ver histórico de migrações
DATABASE_URL="postgresql://postgres:postgres123@localhost:5432/fastapi_auth" uv run alembic history

# Reverter migração
DATABASE_URL="postgresql://postgres:postgres123@localhost:5432/fastapi_auth" uv run alembic downgrade -1
```

### Docker

```bash
# Subir apenas o PostgreSQL
docker compose up -d

# Parar os serviços
docker compose down

# Ver logs do PostgreSQL
docker compose logs postgres
```
