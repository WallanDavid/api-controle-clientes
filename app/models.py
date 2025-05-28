from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    clientes = relationship("Cliente", back_populates="owner")


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True, index=True)
    telefone = Column(String)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="clientes")
    ordens = relationship("OrdemDeServico", back_populates="cliente")


class OrdemDeServico(Base):
    __tablename__ = "ordens"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)
    status = Column(String, default="aberto")

    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    cliente = relationship("Cliente", back_populates="ordens")
