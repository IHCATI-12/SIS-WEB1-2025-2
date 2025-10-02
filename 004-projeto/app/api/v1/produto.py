from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.deps import get_db
# Contrato da api
from app.schemas.produto import ProdutoCreate, ProdutoOut
from app.repositories.produto import create as repo

rotas = APIRouter(prefix="/v1/produto", tags=["produto"])

@rotas.post("/", response_model=ProdutoCreate, status_code=status.HTTP_201_CREATED)
def create(payload: ProdutoCreate, db: Session = Depends(get_db)):
    return repo.create(db, payload)

@rotas.get("/", response_model=list[ProdutoOut])
def list_all(db: Session = Depends(get_db)):
    return repo.get_all(db)

@rotas.get("/", response_model=list[ProdutoOut])
def det_id(produto_id: int,db: Session = Depends(get_db)):
    objeto = repo.get(db, produto_id)
    if not objeto: raise HTTPException(status.HTTP_404_NOT_FOUND, "Produto não encontrado")
    return objeto


