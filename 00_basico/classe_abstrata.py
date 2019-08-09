"""

    'Métodos / Classes Abstratas'

    Exemplo de implementação de métodos abstratos.

    - O fato da classe ter um méotod abstrato, ela se torna abstrata automaticamente. No exemplo abaixo, todas as
    classes que herdarem a classe 'imposto_generico' serão obrigados à implemnetar os método abstratos

    - Nos testes logo abaixo é possível verificar que a classe programa não pode ser instanciada.

"""

from abc import ABCMeta, abstractmethod

class imposto_generico:

    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass


class ISS(imposto_generico):

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05


class ICMS(imposto_generico):

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06

    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False

class Orcamento:

    def __init__(self):
        self.__itens = []

    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total

    @property
    def total_itens(self):
        return len(self.__itens)

    def obter_itens(self):
        return tuple(self.__itens)

    def adicionar_item(self, item):
        self.__itens.append(item)


class Item:

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome


if __name__ == "__main__":

    # As duas classes que herdam de 'imposto_generico' (abstrata)
    iss = ISS()
    icms = ICMS()

    orcamento = Orcamento()
    orcamento.adicionar_item(Item('Item1', 100))
    orcamento.adicionar_item(Item('Item2', 50))

    # Método 'calcula' da Classe Genérica
    print("ISS: ", iss.calcula(orcamento))
    print("ICMS: ", icms.calcula(orcamento))


