from impostos import calcula_icms, calcula_iss

class Calculador_de_impostos:

    def realiza_calculo(self, orcamento, imposto):
        print(imposto(orcamento))


if __name__ == '__main__':

    from orcamento import Orcamento

    calculador = Calculador_de_impostos()

    orcamento = Orcamento(500)

    calculador.realiza_calculo(orcamento, calcula_iss)
    calculador.realiza_calculo(orcamento, calcula_icms)
