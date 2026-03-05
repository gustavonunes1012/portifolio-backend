from pydantic import BaseModel
from typing import List

class Usuario(BaseModel):
    id: int
    nome: str
    email: str


class ItemPedido(BaseModel):
    nome: str
    quantidade: int


class Pedido(BaseModel):
    id: int
    usuario_id: int
    itens: List[ItemPedido]