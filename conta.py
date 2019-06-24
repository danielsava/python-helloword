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

