from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from app import schemas, models
from app.database import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from app.auth import SECRET_KEY, ALGORITHM

router = APIRouter(
    prefix="/ordens",
    tags=["ordens"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciais inválidas",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        raise credentials_exception
    return user

@router.post("/", response_model=schemas.OrdemOut)
def criar_ordem(ordem: schemas.OrdemCreate, cliente_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id, models.Cliente.owner_id == current_user.id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")

    nova_ordem = models.OrdemDeServico(**ordem.dict(), cliente_id=cliente.id)
    db.add(nova_ordem)
    db.commit()
    db.refresh(nova_ordem)
    return nova_ordem

@router.get("/", response_model=list[schemas.OrdemOut])
def listar_ordens(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return (
        db.query(models.OrdemDeServico)
        .join(models.Cliente)
        .filter(models.Cliente.owner_id == current_user.id)
        .all()
    )
