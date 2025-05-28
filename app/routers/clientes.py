from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from app import schemas, models, database
from app.auth import SECRET_KEY, ALGORITHM
from app.database import SessionLocal

router = APIRouter(
    prefix="/clientes",
    tags=["clientes"]
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

@router.post("/", response_model=schemas.ClienteOut)
def criar_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    novo_cliente = models.Cliente(**cliente.dict(), owner_id=current_user.id)
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return novo_cliente

@router.get("/", response_model=list[schemas.ClienteOut])
def listar_clientes(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.Cliente).filter(models.Cliente.owner_id == current_user.id).all()
