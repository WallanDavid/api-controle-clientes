from pydantic import BaseModel
from typing import List, Optional

# --- Usuário ---
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    class Config:
        orm_mode = True


# --- Cliente ---
class ClienteBase(BaseModel):
    nome: str
    email: str
    telefone: str

class ClienteCreate(ClienteBase):
    pass

class ClienteOut(ClienteBase):
    id: int
    class Config:
        orm_mode = True


# --- Ordem de Serviço ---
class OrdemBase(BaseModel):
    descricao: str
    status: Optional[str] = "aberto"

class OrdemCreate(OrdemBase):
    pass

class OrdemOut(OrdemBase):
    id: int
    class Config:
        orm_mode = True


# --- Token JWT ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
