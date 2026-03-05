from fastapi import FastAPI
from fastapi import HTTPException
from schemas import Usuario
from schemas import Pedido
from models import pedidos

from models import usuarios

app = FastAPI()


@app.post("/usuarios")
def criar_usuario(usuario: Usuario):
    for u in usuarios:
        if u.id == usuario.id:
            raise HTTPException(status_code=400, detail="ID já existe")
    usuarios.append(usuario)
    return usuario

@app.get("/usuarios")
def listar_usuarios():
    return usuarios
@app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: int):
    for u in usuarios:
        if u.id == usuario_id:
            return u
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.put("/usuarios/{usuario_id}")
def atualizar_usuario(usuario_id: int, dados: Usuario):
    for i, u in enumerate(usuarios):
        if u.id == usuario_id:
            usuarios[i] = dados
            return dados
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int):
    for i, u in enumerate(usuarios):
        if u.id == usuario_id:
            usuarios.pop(i)
            return {"detail": "Usuário removido"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")


@app.post("/pedidos")
def criar_pedido(pedido: Pedido):
    pedidos.append(pedido)
    return pedido


@app.get("/pedidos")
def listar_pedidos():
    return pedidos