from fastapi import FastAPI, HTTPException
from schemas import Usuario, Pedido, ItemPedido
from models import usuarios, pedidos

app = FastAPI()

# -------------------------------
# CRUD de Usuários
# -------------------------------

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

# -------------------------------
# CRUD de Pedidos
# -------------------------------

@app.post("/pedidos")
def criar_pedido(pedido: Pedido):
    if not any(u.id == pedido.usuario_id for u in usuarios):
        raise HTTPException(status_code=400, detail="Usuário não encontrado")
    for p in pedidos:
        if p.id == pedido.id:
            raise HTTPException(status_code=400, detail="ID do pedido já existe")
    pedidos.append(pedido)
    return pedido

@app.get("/pedidos")
def listar_pedidos():
    return pedidos

@app.get("/pedidos/{pedido_id}")
def buscar_pedido(pedido_id: int):
    for p in pedidos:
        if p.id == pedido_id:
            return p
    raise HTTPException(status_code=404, detail="Pedido não encontrado")

@app.put("/pedidos/{pedido_id}")
def atualizar_pedido(pedido_id: int, dados: Pedido):
    for i, p in enumerate(pedidos):
        if p.id == pedido_id:
            pedidos[i] = dados
            return dados
    raise HTTPException(status_code=404, detail="Pedido não encontrado")

@app.delete("/pedidos/{pedido_id}")
def deletar_pedido(pedido_id: int):
    for i, p in enumerate(pedidos):
        if p.id == pedido_id:
            pedidos.pop(i)
            return {"detail": "Pedido removido"}
    raise HTTPException(status_code=404, detail="Pedido não encontrado")