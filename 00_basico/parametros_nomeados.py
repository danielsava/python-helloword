"""
    Parâmetros Nomeados: O Python permite que o nome dos parâmetros possam ser informados, dessa forma identificando-os
                         na passagem de parâmetros, evitando com isso possível erros.
                         Usando parâmetros nomeados, eles não precisam estar na ordem.

"""

from datetime import date


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


    def __init__(self, razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes=''):
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


if __name__ == '__main__':

    itens = [Item('ItemA', 100), Item('ItemB', 200)]

    # Uso de Parâmetros Nomeados. Dessa forma, a ordem dos paramêtros não precisa estar na ordem
    nota_fiscal = NotaFiscal(itens=itens, cnpj='62.184.535/0001-17', razao_social='SavaLtda')

