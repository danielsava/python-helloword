"""
   Classe Mae : Programa
"""


class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._likes = 0
        self.ano = ano


    def dar_likes(self):
        self._likes += 1


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    @property
    def likes(self):
        return self._likes



"""
    Classe Filha : Filme

"""

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao



"""
    Classe Filha : Serie

"""

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


"""
    'hasattr' : Verifica se existe o atribuito de um objeto

"""


vingadores = Filme('VingadorES - GUErra Infinita', 2018, 160)
vingadores.dar_likes()
vingadores.dar_likes()

atlanta = Serie('Atlanta', 2017, 2)

atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas # **** 'hasattr' ****
    print(f'{programa.nome} : {detalhes} Temporadas : {programa.likes} likes')
