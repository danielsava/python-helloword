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
    Testes

"""


vingadores = Filme('VingadorES - GUErra Infinita', 2018, 160)
print(f'FILME : Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')

vingadores.dar_likes()
vingadores.dar_likes()
print(f'FILME : Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')

atlanta = Serie('Atlanta', 2017, 2)
print(f'SERIE : Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')

atlanta.dar_likes()
print(f'SERIE : Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    print(programa)
