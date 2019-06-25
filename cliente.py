

class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("Chamando 'get' do atributo 'nome'")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("Chamando 'set' do atributo 'nome'")
        self.__nome = nome
