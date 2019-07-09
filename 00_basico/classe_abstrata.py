"""

    'Métodos / Classes Abstratas'

    Exemplo de implementação de métodos abstratos.

    - O fato da classe ter um méotod abstrato, ela se torna abstrata automaticamente. No exemplo abaixo, todas as
    classes que herdarem a classe 'Programa' serão obrigados à implemnetar o método abstrato '__str__'

    - Nos testes logo abaixo é possível verificar que a classe programa não pode ser instanciada.

"""

from abc import ABCMeta, abstractmethod


class Programa(metaclass=ABCMeta):

    @abstractmethod
    def __str__(self):
        pass



"""
    Testes
"""

p1 = Programa()

print(p1)
