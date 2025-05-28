from fastapi import FastAPI
from app.routers import users, clientes, ordens

app = FastAPI(
    title="API de Controle de Clientes",
    description="Sistema com JWT, usuários, clientes e ordens de serviço",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(clientes.router)
app.include_router(ordens.router)

@app.get("/")
def read_root():
    return {"message": "API de Controle de Clientes rodando!"}
