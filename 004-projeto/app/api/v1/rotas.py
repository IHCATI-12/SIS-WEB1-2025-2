from fastapi import APIRouter
from . import produto, categoria


api_rotas = APIRouter()
api_rotas.include_router(produto.rotas)
api_rotas.include_router(categoria.rotas)
