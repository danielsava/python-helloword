# Comentário uma linha

'''
    Comentário múltipla linha

'''

# Python é case-sensitive

'''
    Conversões:
        - str(a): converte para string

    Tipos
        - Numéricos
           - int: int(x)
           - float: float(x)
           - complex: complex(x)

        - None

        - Bool
            - bool: bool(x)

        - String
            - string: str(x)

    Listas
        - list() ou []
            * append()
            * remove()
            * clear()
            * copy()


'''

# Anotação

import time

def log(fun):                   # O argumento 'fun' é a função que foi anotada
    def wrapper(t):             # O argumento 't' são os argumentos da função que foi anotada 
        t0 = time.time()
        fun(t)
        t1 = time.time()
        print('Essa função levou ' + str(t1 - t0))
    return wrapper

@log
def soneca(t):
    time.sleep(t)



# Lista

lista = [1, 2, 3]

for x in lista:
    print(x)



# Dicionario

dic = {
    'chave-1': 5,
    'chave-2': 10
}

for x in dic:
    print(x)


# Exception

try:
    y = 10 / x
except:
    print('falhou')


# Input
x = input('Informe o valor: ')
    



