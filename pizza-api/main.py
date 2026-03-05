from fastapi import FastAPI
from fastapi import HTTPException
from schemas import Usuario
from schemas import Pedido
from models import pedidos

from models import usuarios

app = FastAPI()


@app.post("/usuarios")
def criar_usuario(usuario: Usuario):
    usuarios.append(usuario)
    return usuario


@app.get("/usuarios")
def listar_usuarios():
    return usuarios



@app.post("/pedidos")
def criar_pedido(pedido: Pedido):
    pedidos.append(pedido)
    return pedido


@app.get("/pedidos")
def listar_pedidos():
    return pedidos