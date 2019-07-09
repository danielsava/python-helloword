class Funcionario:

    def __init__(self, nome):
        self.nome = nome


    def registrar_horas(self, horas):
        print('Horas registradas ... ')

    def mostrar_tarefas(self):
        print('Fez muita coisa')


class Caelum(Funcionario):

    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def buscar_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')


class Alura(Funcionario):

    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete !')

    def buscar_perguntas_sem_respostas(self):
        print('Mostrando perguntas não respondidas do forum')



'''
    MIXIN: 
        - São as classes que existem apenas para adicionar um comportamento, e não para serem, necessariamente, 
    instanciada. Por exemplo, a classe 'Hipster' abaixo existe para sobrescrever o 'toString' (do Python). As classes
    que herdarem será apenas para ter esse comportamento em específico.
'''
class Hipster:

    def __str__(self):
        return f'Hispter, {self.nome}'



'''
    Herança Multipla:
        - Classes Pleno e Senior
    
'''

class Junior(Alura):
    pass


class Pleno(Alura, Caelum, Hipster):
    pass



'''
    Testes
'''

# Funcionário 'Junior'
jose = Junior('Jose')
print(' #### Funcionário Junior ####')

print('\nMétodo Sobrescrito na Classe Alura')
jose.mostrar_tarefas()

print('\nMétodo da Classe')
jose.buscar_perguntas_sem_respostas()


# Funcionário 'Pleno'
luan = Pleno('Luan')
print(' #### Funcionário Pleno ####')

luan.buscar_cursos_do_mes()

luan.buscar_perguntas_sem_respostas()

# Por padrão, decidiu mostrar o método da implementado na Alura.
#   - O Python utiliza uma GAMBIARRA chamada algoritmo 'MRO'
luan.mostrar_tarefas()

# Herda o comportamento '__str__' da classe Hipster
print(luan)







