from banco import Banco

class Operacoes:
    def __init__(self, banco):
        self.banco = banco

    def depositar(self, nome, valor):
        cliente = self.banco.buscar_cliente(nome)
        if cliente:
            cliente.saldo += valor
            print(f"Depósito de {valor} realizado. Saldo: {cliente.saldo}")
        else:
            print("Cliente não encontrado")

    def sacar(self, nome, valor):
        cliente = self.banco.buscar_cliente(nome)
        if cliente:
            if valor <= cliente.saldo:
                cliente.saldo -= valor
                print(f"Saque de {valor} realizado. Saldo: {cliente.saldo}")
            else:
                print("Saldo insuficiente")
        else:
            print("Cliente não encontrado")

    def transferir(self, origem_nome, destino_nome, valor):
        origem = self.banco.buscar_cliente(origem_nome)
        destino = self.banco.buscar_cliente(destino_nome)
        if origem and destino:
            if valor <= origem.saldo:
                origem.saldo -= valor
                destino.saldo += valor
                print("Transferência realizada")
            else:
                print("Saldo insuficiente")
        else:
            print("Conta origem ou destino não encontrada")