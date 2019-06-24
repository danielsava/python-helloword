"""

    Para o paradigma de Orientação à Objetos, o python prega como boa prática o padrão CamelCase

"""


class Conta:

    """
        Construtores
    """
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo Conta {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def __init__(self, numero, titular, saldo, limite = 1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


