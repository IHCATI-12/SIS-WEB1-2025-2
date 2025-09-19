from sqlalchemy.orm import Session
# tabela produto
from app.models.produto import Produto
# contrato da API
from app.schemas.produto import ProdutoCreate,ProdutoUpdate,ProdutoOut

def create(db: Session, payload: ProdutoCreate) -> Produto:
    objeto = Produto(**payload.model_dump()) 
    db.add(objeto) 
    db.commit()
    db.refresh(objeto)   
    return objeto


