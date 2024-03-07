# API CRUD de Cartão de Vacina em Python

CRUD (Create, Read, Update, Delete) em registros de cartões de vacinação. A API é construída utilizando o framework Flask e SQLAlchemy para interagir com um banco de dados PostgreSQL. Abaixo estão as instruções para configurar, utilizar e testar a API.

## Configuração

### Requisitos

Certifique-se de ter as seguintes dependências instaladas:

- Python (3.6 ou superior)
- Flask
- SQLAlchemy
- psycopg2
- Git

### Configuração do Banco de Dados

A API utiliza um banco de dados PostgreSQL. Certifique-se de ter um servidor PostgreSQL em execução e configure as informações de conexão no arquivo `app/configs/database.py`.

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

## Estrutura do Projeto

O projeto está estruturado da seguinte maneira:

```
|-- app
|   |-- configs
|   |   |-- database.py
|   |-- models
|   |   |-- vaccine_model.py
|   |-- routes
|   |   |-- vaccine_routes.py
|   |-- __init__.py
|-- tests
|-- .gitignore
|-- app.py
|-- requirements.txt
|-- README.md
```

- **app/configs/database.py**: Configuração do banco de dados.
- **app/models/vaccine_model.py**: Definição do modelo de cartões de vacina utilizando SQLAlchemy.
- **app/routes/vaccine_routes.py**: Implementação das rotas CRUD da API.
- **tests**: Diretório para testes (opcional).
- **app.py**: Arquivo principal para iniciar a aplicação.
- **requirements.txt**: Lista de dependências.

## API CRUD

### 1. Criação de Cartão de Vacina

Endpoint: `POST /vaccine-cards`

#### Payload de Exemplo

```json
{
  "cpf": "12345678901",
  "name": "Maria Silva",
  "vaccine_name": "COVID-19 Vaccine",
  "health_unit_name": "City Health Center"
}
```

#### Resposta de Exemplo (201 Created)

```json
{
  "cpf": "12345678901",
  "name": "Maria Silva",
  "first_shot_date": "2024-03-07T12:00:00",
  "second_shot_date": "2024-06-05T12:00:00",
  "vaccine_name": "COVID-19 Vaccine",
  "health_unit_name": "City Health Center"
}
```

### 2. Obter Todos os Cartões de Vacina

Endpoint: `GET /vaccine-cards`

#### Resposta de Exemplo (200 OK)

```json
[
  {
    "cpf": "12345678901",
    "name": "Maria Silva",
    "first_shot_date": "2024-03-07T12:00:00",
    "second_shot_date": "2024-06-05T12:00:00",
    "vaccine_name": "COVID-19 Vaccine",
    "health_unit_name": "City Health Center"
  }
]
```

## Como Clonar e Testar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Instale as dependências:

```bash
cd nome-do-projeto
pip install -r requirements.txt
```

3. Configure o banco de dados no arquivo `app/configs/database.py`.

4. Execute a aplicação:

```bash
python app.py
```

A aplicação estará disponível em `http://localhost:5000`.

### Testes (Opcional)

Para executar testes (caso disponíveis), você pode usar o seguinte comando:

```bash
pytest
```

Certifique-se de ter o módulo `pytest` instalado.

Agora você pode interagir com a API CRUD de cartões de vacina em Python!
