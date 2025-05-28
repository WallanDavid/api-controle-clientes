# 💼 API de Controle de Clientes

![Docker](https://img.shields.io/badge/docker-ready-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-brightgreen)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![License](https://img.shields.io/github/license/WallanDavid/api-controle-clientes)

Sistema de gerenciamento de clientes e ordens de serviço com autenticação JWT. Ideal para portfólio e aplicações reais.

---

## 🚀 Tecnologias

- **FastAPI** — API moderna com OpenAPI (Swagger)
- **JWT Auth** — Login seguro via token
- **SQLite** — Banco de dados local simples
- **Docker & Compose** — Containerização rápida
- **Uvicorn** — Servidor leve e performático
- **Pydantic v2** — Validação com dataclasses modernas

---

## 🔧 Funcionalidades

- Registro e login de usuários
- Geração e verificação de token JWT
- CRUD de clientes
- CRUD de ordens de serviço (vinculadas a clientes)
- Documentação Swagger gerada automaticamente

---

## ▶️ Como rodar com Docker

```bash
git clone https://github.com/WallanDavid/api-controle-clientes.git
cd api-controle-clientes
docker-compose up --build
```

Acesse a documentação em:
📚 **http://localhost:8000/docs**

---

## 🧪 Endpoints principais

| Método | Rota                          | Descrição                      |
|--------|-------------------------------|--------------------------------|
| POST   | `/users/register`             | Registro de usuário            |
| POST   | `/users/login`                | Login e obtenção do token JWT  |
| GET    | `/clientes/`                  | Lista todos os clientes        |
| POST   | `/clientes/`                  | Cria um cliente novo           |
| GET    | `/ordens/`                    | Lista ordens de serviço        |
| POST   | `/ordens/?cliente_id=1`       | Cria nova ordem p/ cliente     |

---

## 🔐 Autenticação

1. Faça login via `/users/login`
2. Copie o token retornado
3. No Swagger, clique em **Authorize** e cole o token com o prefixo:
   `Bearer <seu_token>`

---

## 🌐 GitHub Pages

A demo explicativa (em breve) estará disponível em:
**https://WallanDavid.github.io/api-controle-clientes**

---

## 🤝 Contribuições

Aberto a melhorias, refatorações e ideias novas.
Pull Requests são bem-vindos!

---

## 📄 Licença

Este projeto está sob a licença MIT.
