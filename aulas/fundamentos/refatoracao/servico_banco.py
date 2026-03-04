from banco import Banco
from operacoes_refatorado import Operacoes

class ServicoBanco:
    def __init__(self, banco):
        self.banco = banco
        self.operacoes = Operacoes()

    def depositar(self, nome, valor):
        cliente = self.banco.buscar_cliente(nome)
        if cliente and self.operacoes.depositar(cliente, valor):
            return True
        return False

    def sacar(self, nome, valor):
        cliente = self.banco.buscar_cliente(nome)
        if cliente and self.operacoes.sacar(cliente, valor):
            return True
        return False

    def transferir(self, origem_nome, destino_nome, valor):
        origem = self.banco.buscar_cliente(origem_nome)
        destino = self.banco.buscar_cliente(destino_nome)
        if origem and destino and self.operacoes.transferir(origem, destino, valor):
            return True
        return False