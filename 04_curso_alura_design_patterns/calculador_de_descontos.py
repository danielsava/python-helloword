
class CalculadorDescontos:

    def calcula(self, orcamento):
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        elif orcamento.valor > 500:
            return orcamento.valor * 0.07


if __name__ == "__main__":

    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adicionar_item(Item('Item1', 100))
    orcamento.adicionar_item(Item('Item2', 50))
    orcamento.adicionar_item(Item('Item3', 400))

    print("Orçamento: ", orcamento.valor)

    calculador = CalculadorDescontos()

    desconto_calculado = calculador.calcula(orcamento)

    print("Desconto: ", desconto_calculado)


