from sqlalchemy.orm import Session
# tabela categoria
from app.models.categoria import Categoria
# contrato da API
from app.schemas.categoria import CategoriaCreate

def create(db: Session, payload: CategoriaCreate) -> Categoria:
    objeto = Categoria(**payload.model_dump()) # Associar atributos iguais
    db.add(objeto) 
    db.commit()
    db.refresh(objeto)   
    return objeto

def get(db: Session, categoria_id: int) -> Categoria | None:
    return db.get(Categoria, categoria_id)
 
def get_all(db: Session) -> list[Categoria]:
    return db.query(Categoria).order_by(Categoria.id).all()