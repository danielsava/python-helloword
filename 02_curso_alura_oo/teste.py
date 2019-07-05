class Listinha:

    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return self.items.__iter__()

    '''
    def __len__(self):
        return len(self.items)
    '''


meu_objeto = Listinha([1, 2, 4])

contador = 0

for item in meu_objeto:
    contador += 1
    print(item)


if len(meu_objeto) == contador:
    print('São Iguais !')
else:
    print('Não são iguais !')


