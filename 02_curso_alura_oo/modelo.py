"""
   Modelo : Programa
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

    # Sobrescrita do 'toString' do Python
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} likes'


"""
    Modelo : Filme

"""

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    # Sobrescrita do 'toString' do Python
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} likes'


"""
    Modelo : Serie

"""

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    # Sobrescrita do 'toString' do Python
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} likes'


"""
    Modelo : Serie

"""

class PlayList:

    def __init__(self, nome, programas):
        self.nome = nome
        self.__programas = programas

    ''' 
        Torna a PlayList uma classe ITERÁVEL (iterable) e com isso passa a ter suporte à diversos 
        recursos como o 'FOR', o 'IN', o acesso à lista por índice ( ex.: playlist_x[0] )
         
    '''
    def __getitem__(self, item):
        return self.__programas[item]

    '''
        Torna a classe um 'sized', podendo utilizar o 'len' para saber o tamanho da lista de programas
    '''
    def __len__(self):
        return len(self.__programas)

    @property
    def listagem(self):
        return self.__programas



"""
    Testes

"""

print("")

vingadores = Filme('VingadorES - GUErra Infinita', 2018, 160)

atlanta = Serie('Atlanta', 2017, 2)

tmep = Filme('Todo mundo em Pânico', 1999, 100)

demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()

demolidor.dar_likes()
demolidor.dar_likes()

print("")

# Lista mantem a ordem de inserção dos elementos
filmes_e_series = [vingadores, atlanta, demolidor, tmep]

# O modelo 'PlayList' herdou de 'list' portanto possui um iterable e outras funcionalidades do List, como o 'len'
playlist_fim_de_semana = PlayList('Fim de semana', filmes_e_series)

print(f'Tamanho da PlayList: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Ta ou não tá ? {demolidor in playlist_fim_de_semana}')

