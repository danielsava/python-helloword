"""

    Atributo Privado
    '__' : Dois underscore em Python é o 'private' do Java. Ou seja, caso queira que uma atributo seja privado
           basta adicionar esses dois underscore no nome do atributo.

    Limpando referência de Memória
    'None': limpa a referência de um objeto
        - conta = new Conta(1, 'João', 500.0)
        - c1 = conta
        - conta = None          # Limpou a referência de 'conta'. Está 'vazia'

"""


class Conta:


    """
        Construtores
    """

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo Conta {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    """
        Métodos
    """

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def imprimir_extrato(self):
        print("Saldo de {} do titular {}.".format(self.__saldo, self.__titular))


    """
        Get / Set
    """

    @property
    def numero(self):
        print("Chamando 'get' de 'numero'")
        return self.__numero

    @property
    def titular(self):
        print("Chamando 'get' de 'titular'")
        return self.__titular

    @property
    def saldo(self):
        print("Chamando 'get' de 'saldo'")
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        print("Chamando 'set' de 'saldo'")
        self.__saldo = saldo

    @property
    def limite(self):
        print("Chamando 'get' de 'limite'")
        return self.__limite

    @limite.setter
    def limite(self, limite):
        print("Chamando 'set' de 'limite'")
        self.__limite = limite

