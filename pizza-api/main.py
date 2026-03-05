from fastapi import FastAPI
from schemas import Usuario
from models import usuarios

app = FastAPI()


@app.post("/usuarios")
def criar_usuario(usuario: Usuario):
    usuarios.append(usuario)
    return usuario


@app.get("/usuarios")
def listar_usuarios():
    return usuarios

from schemas import Pedido
from models import pedidos


@app.post("/pedidos")
def criar_pedido(pedido: Pedido):
    pedidos.append(pedido)
    return pedido


@app.get("/pedidos")
def listar_pedidos():
    return pedidos