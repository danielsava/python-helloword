"""

    Atributo ou Método Privado
    '__' : Dois underscore em Python é o 'private' do Java. Ou seja, caso queira que uma atributo ou método seja privado
           basta adicionar esses dois underscore antes do no nome do atributo ou do método.

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

    def imprimir_extrato(self):
        print("Saldo de {} do titular {}.".format(self.__saldo, self.__titular))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite da conta".format(valor))



    """ 
        Método PRIVADO 
    """
    def __pode_sacar(self, valor):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor <= valor_disponivel_a_sacar



    """
        Métodos Estáticos
            
    """
    # - Para acessar, digite: 'Conta.codigo_banco()'
    @staticmethod
    def codigo_banco():
        return '001'

    # Neste caso para acessar:
    # - codigos = Conta.codigos_bancos()
    # - codg_caixa = codigos['Caixa']
    @staticmethod
    def codigos_banco():
        return {'Banco do Brasil': '001', 'Caixa': '104', 'Bradesco': '237'}



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

