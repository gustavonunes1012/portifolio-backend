class Operacoes:
    def depositar(self, cliente, valor):
        if valor <= 0:
            return False
        cliente.saldo += valor
        return True

    def sacar(self, cliente, valor):
        if 0 < valor <= cliente.saldo:
            cliente.saldo -= valor
            return True
        return False

    def transferir(self, origem, destino, valor):
        if 0 < valor <= origem.saldo:
            origem.saldo -= valor
            destino.saldo += valor
            return True
        return False