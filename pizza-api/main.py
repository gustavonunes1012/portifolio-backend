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