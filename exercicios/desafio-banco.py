contas = []

def criar_conta():
    nome = input("Digite o nome do titular: ")
    saldo = 0
    conta = {"titular": nome, "saldo": saldo}
    contas.append(conta)
    print(f"Conta criada para {nome} com saldo {saldo}")

def consultar_conta():
    nome = input("Digite o nome do titular: ")
    for conta in contas:
        if conta["titular"] == nome:
            print(f"Titular: {conta['titular']}, Saldo: {conta['saldo']}")
            return conta
    print("Conta não encontrada")
    return None

def depositar():
    conta = consultar_conta()
    if conta:
        valor = float(input("Digite o valor a depositar: "))
        if valor > 0:
            conta["saldo"] += valor
            print(f"Novo saldo: {conta['saldo']}")
        else:
            print("Valor inválido")

def sacar():
    conta = consultar_conta()
    if conta:
        valor = float(input("Digite o valor a sacar: "))
        if 0 < valor <= conta["saldo"]:
            conta["saldo"] -= valor
            print(f"Novo saldo: {conta['saldo']}")
        else:
            print("Saldo insuficiente ou valor inválido")

def transferir():
    print("Conta de origem:")
    origem = consultar_conta()
    if origem:
        print("Conta de destino:")
        destino = consultar_conta()
        if destino:
            valor = float(input("Digite o valor a transferir: "))
            if 0 < valor <= origem["saldo"]:
                origem["saldo"] -= valor
                destino["saldo"] += valor
                print("Transferência realizada com sucesso")
            else:
                print("Saldo insuficiente ou valor inválido")

def listar_contas():
    if contas:
        for conta in contas:
            print(f"Titular: {conta['titular']}, Saldo: {conta['saldo']}")
    else:
        print("Nenhuma conta cadastrada")

while True:
    print("\n=== Banco Python ===")
    print("1 - Criar conta")
    print("2 - Consultar conta")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Transferir")
    print("6 - Listar contas")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        criar_conta()
    elif opcao == "2":
        consultar_conta()
    elif opcao == "3":
        depositar()
    elif opcao == "4":
        sacar()
    elif opcao == "5":
        transferir()
    elif opcao == "6":
        listar_contas()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida")