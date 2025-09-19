from pydantic import BaseModel, ConfigDict
from typing import Optional

class ProdutoCreate(BaseModel):
    nome: str
    preco: float
    categoria_id: int

class ProdutoOut(BaseModel):
    id: int
    nome: str
    preco: float
    categoria_id: int
    model_config = ConfigDict(from_attributes=True)
    
class ProdutoUpdate(BaseModel):
    nome: Optional[str] = None
    preco: Optional[int] = None 
    categoria: Optional[int] = None
    
    
    
    