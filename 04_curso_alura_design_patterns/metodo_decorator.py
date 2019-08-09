'''
    Exemplo NAO FUNFO

'''

# Funcao Decorator, que irá receber uma Função ou Método em seu argumento
def metodo_decorator_soma_05(metodo_ou_funcao):
    def wrapper(self, outro_valor):
        print("Antes Calcular")
        retorno_metodo_decorado = metodo_ou_funcao(self, outro_valor)
        return retorno_metodo_decorado + 100
    return wrapper

def imprimir_destaque(funcao):
    def wrapper(self):
        print('*****')
        funcao(self)
        print('*****')
    return wrapper


class Exemplo1:

    def __init__(self, valor):
        self.__valor = valor

    def somar(self, outro_valor):
        return self.__valor + outro_valor + 10

    def imprimir_valor(self):
        print(self.__valor)


class Exemplo2:

    def __init__(self, valor):
        self.__valor = valor

    @metodo_decorator_soma_05
    def somar(self, outro_valor):
        return self.__valor + outro_valor + 20

    @imprimir_destaque
    def imprimir_valor(self):
        print(self.__valor)


class Exemplo3:

    def __init__(self, valor):
        self.__valor = valor

    @metodo_decorator_soma_05
    def somar(self, outro_valor):
        return self.__valor + outro_valor + 30

    @imprimir_destaque
    def imprimir_valor(self):
        print(self.__valor)


if __name__ == "__main__":

    print("Exemplo Decorator")

    ex1 = Exemplo1(1)
    print(ex1.somar(1))
    ex1.imprimir_valor()

    ex2 = Exemplo1(2)
    print(ex2.somar(1))
    ex2.imprimir_valor()

    ex3 = Exemplo1(3)
    print(ex3.somar(1))
    ex3.imprimir_valor()
