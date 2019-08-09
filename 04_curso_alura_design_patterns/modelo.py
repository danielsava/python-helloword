
from abc import ABCMeta, abstractmethod     # Classes Abstratas
from datetime import date                   # Datas no Python


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


'''
    Design Pattern: State
'''

class estado_orcamento_generico:

    __metaclass__ = ABCMeta

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass

    @abstractmethod
    def finaliza(self, orcamento):
        pass

class Em_Aprovacao(estado_orcamento_generico):

    def aplica_desconto_extra(self, orcamento):
        orcamento.desconto_extra = orcamento.valor * 0.02

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception('Orçamento em aprovação nao pode ser finalizado')

    def __str__(self):
        return "Em Aprovação"



class Aprovado(estado_orcamento_generico):

    def aplica_desconto_extra(self, orcamento):
        orcamento.desconto_extra = orcamento.valor * 0.05

    def aprova(self, orcamento):
        raise Exception('Orçamento já está aprovado')

    def reprova(self, orcamento):
        raise Exception("Orçamento já está aprovado, por isso não pode ser 'reprovado'")

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

    def __str__(self):
        return "Aprovado"


class Reprovado(estado_orcamento_generico):

    def aplica_desconto_extra(self, orcamento):
        raise Exception("Orçamento 'reprovado' não possui desconto extra")

    def aprova(self, orcamento):
        raise Exception("Orçamento 'reprovado' não pode ser 'aprovado'")

    def reprova(self, orcamento):
        raise Exception("Orçamento já está 'reprovado'")

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

    def __str__(self):
        return "Reprovado"

class Finalizado(estado_orcamento_generico):

    def aplica_desconto_extra(self, orcamento):
        raise Exception("Orçamento 'finalizado' não possui desconto extra ")

    def aprova(self, orcamento):
        raise Exception("Orçamento já está 'finalizado', não pode ser 'aprovado'")

    def reprova(self, orcamento):
        raise Exception("Orçamento já está 'finalizado', não pode ser 'reprovado'")

    def finaliza(self, orcamento):
        raise Exception("Orçamento já está 'finalizado'")

    def __str__(self):
        return "Finalizado"


'''
    Fim : Design Pattern State 
'''


class Orcamento:

    """ Foi substituidas pelas Classes acimas, representando a implementação do Padrão 'State'
    EM_APROVACAO = 1
    APROVADO = 2
    REPROVADO = 3
    FINALIZADO = 4
    """

    def __init__(self):
        self.__itens = []
        self.__desconto_extra = 0
        self.estado_atual = Em_Aprovacao() # Orcamento.EM_APROVACAO


    """
    def aplica_desconto_extra(self):
        if self.estado_atual == Orcamento.EM_APROVACAO:
            self.__desconto_extra = self.valor * 0.02
        elif self.estado_atual == Orcamento.APROVADO:
            self.__desconto_extra = self.valor * 0.05
        elif self.estado_atual == Orcamento.REPROVADO:
            raise Exception("Orçamento 'reprovado' não possui desconto extra")
        elif self.estado_atual == Orcamento.FINALIZADO:
            raise Exception("Orçamento 'finalizado' não possui desconto extra ")
    """

    def aprova(self):
        self.estado_atual.aprova(orcamento)

    def reprova(self):
        self.estado_atual.reprova(orcamento)

    def finaliza(self):
        self.estado_atual.finaliza(orcamento)


    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total - self.__desconto_extra

    @property
    def total_itens(self):
        return len(self.__itens)

    @property
    def desconto_extra(self):
        return self.__desconto_extra

    @desconto_extra.setter
    def desconto_extra(self, valor):
        self.__desconto_extra = valor

    def obter_itens(self):
        return tuple(self.__itens)

    def adicionar_item(self, item):
        self.__itens.append(item)


class Item:

    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def descricao(self):
        return self.__descricao



class NotaFiscal:


    def __init__(self, razao_social, cnpj, itens, data_de_emissao, detalhes):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception('Detalhes da Nota não pode ter mais que 20 caracteres')
        self.__detalhes = detalhes
        self.__itens = itens

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes


""" Design Pattern: Builder """


class CriadorNotaFiscal:

    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None
        self.__data_de_emissao = date.today()
        self.__itens = None
        self.__detalhes = ''


    def com_razao_social(self, razao_social):
        self.__razao_social = razao_social
        return self

    def com_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def com_data_de_emissao(self, data_de_emissao):
        self.__data_de_emissao = data_de_emissao
        return self

    def com_itens(self, itens):
        self.__itens = itens
        return self

    def com_detalhes(self, detalhes):
        self.__detalhes = detalhes
        return self

    def constroi(self):

        if self.__razao_social is None:
            raise Exception("'Razão Social' obrigatório")
        elif self.__cnpj is None:
            raise Exception("'Cnpj' obrigatório")
        elif self.__itens is None:
            raise Exception("'Itens' obrigatório")

        return NotaFiscal(
                razao_social=self.__razao_social,
                cnpj=self.__cnpj,
                data_de_emissao=self.__data_de_emissao,
                itens=self.__itens,
                detalhes=self.__detalhes
              )






if __name__ == '__main__':




    itens = [Item('ItemA', 100), Item('ItemB', 200)]

    # Uso de Parâmetros Nomeados. Dessa forma, a ordem dos paramêtros não precisa estar na ordem
    nota_fiscal = NotaFiscal(razao_social='SavaLtda', cnpj='62.184.535/0001-17', itens=itens, data_de_emissao=date.today(), detalhes='')
    print(nota_fiscal)

    # NotaFiscal criada com Builder
    nota_fiscal2 = (CriadorNotaFiscal()
                    .com_razao_social('SavaFilialLtda')
                    .com_cnpj('62.184.535/0001-17')
                    .com_itens(itens)).constroi()

    print(nota_fiscal2)

