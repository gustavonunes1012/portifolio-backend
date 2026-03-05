from pydantic import BaseModel, EmailStr, validator
from typing import List

class Usuario(BaseModel):
    id: int
    nome: str
    email: EmailStr

    @validator('nome')
    def nome_minimo(cls, v):
        if len(v.strip()) < 2:
            raise ValueError('Nome deve ter pelo menos 2 caracteres')
        return v

class ItemPedido(BaseModel):
    nome: str
    quantidade: int

    @validator('nome')
    def nome_nao_vazio(cls, v):
        if not v.strip():
            raise ValueError('Nome do item não pode ser vazio')
        return v

    @validator('quantidade')
    def quantidade_maior_que_zero(cls, v):
        if v <= 0:
            raise ValueError('Quantidade deve ser maior que 0')
        return v

class Pedido(BaseModel):
    id: int
    usuario_id: int
    itens: List[ItemPedido]

    @validator('itens')
    def deve_ter_itens(cls, v):
        if len(v) == 0:
            raise ValueError('Pedido deve ter pelo menos um item')
        return v