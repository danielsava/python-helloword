
def criar_conta(numero, titular, saldo, limite):
    return {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}


def depositar(conta, valor):
    conta["saldo"] += valor


def sacar(conta, valor):
    conta["saldo"] -= valor


def imprimir_extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))

