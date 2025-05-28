📦 API de Controle de Clientes
API RESTful desenvolvida com FastAPI, JWT e SQLAlchemy para gerenciamento de usuários, clientes e ordens de serviço. Protegida com autenticação e documentação automática via Swagger.

🚀 Funcionalidades
Cadastro e login de usuários

Autenticação com JWT

CRUD de clientes (vinculados ao usuário)

CRUD de ordens de serviço (vinculadas a clientes)

Documentação automática com Swagger UI

Banco local com SQLite

🛠️ Tecnologias utilizadas
FastAPI

Uvicorn

SQLAlchemy

Pydantic

python-jose

passlib

SQLite

💻 Como rodar localmente

1. Clone o repositório
git clone <https://github.com/SEU-USUARIO/api-controle-clientes.git>
cd api-controle-clientes

2. Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate (Windows)

3. Instale as dependências
pip install -r requirements.txt

4. Crie o banco de dados
python -m app.create_db

5. Inicie o servidor
uvicorn app.main:app --reload

🔐 Autenticação
Registre um usuário com POST /users/register

Faça login com POST /users/login e copie o access_token

Clique em "Authorize" na Swagger UI e cole assim:
Bearer SEU_TOKEN_AQUI

📑 Endpoints principais
Usuários
POST /users/register → Cadastrar usuário

POST /users/login → Login com JWT

Clientes
POST /clientes/ → Criar cliente

GET /clientes/ → Listar clientes

Ordens de Serviço
POST /ordens/?cliente_id=ID → Criar OS

GET /ordens/ → Listar OS

🔍 Teste via Swagger
Acesse: <http://127.0.0.1:8000/docs>

📝 Licença
Projeto livre sob licença MIT.

Desenvolvido por Wallan David 🚀
