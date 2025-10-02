from sqlalchemy.orm import Session
# tabela produto
from app.models.produto import Produto
# contrato da API
from app.schemas.produto import ProdutoCreate

def create(db: Session, payload: ProdutoCreate) -> Produto:
    # objeto = Produto(nome=payload.nome, preco=payload.preco,)
    objeto = Produto(**payload.model_dump()) 
    db.add(objeto) 
    db.commit()
    db.refresh(objeto)   
    return objeto

def get(db: Session, produto_id: int) -> Produto | None:
    return db.get(Produto, produto_id)
 
def get_all(db: Session) -> list[Produto]:
    return db.query(Produto).order_by(Produto.nome).all()

