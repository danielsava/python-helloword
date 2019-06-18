"""

    Para declarar uma função no Python deve ser utilizado a palavra 'def' seguido do nome da função
    obdecendo (aconselhável) o padrão 'snake_case'.

"""


def nome_da_funcao():
    print("Função declarada e executada")


# Parametros e retorno
def soma(a, b):
    return a + b


# Para ser executado somente quando o script for executado diretamente
if __name__ == "__main__":
    nome_da_funcao()
    s = soma(5, 8)
    print("Resultado da Soma: ", s)

'''
    *** Argumento OPCIONAL ***
        - Python permite a criação de funções onde a passagem de parâmetros é opcional. Na verdade, você seta um valor
        default para o argumento atribuindo um valor à ele na definção da função. Caso nenhum valor seja passado à 
        função, será utilizado o valor definido.
'''


def criar_arquivo_txt(nome_arquivo='teste.txt'):
    arquivo = open(nome_arquivo, 'w')
    arquivo.close()


# Cria um arquivo com o nome 'default', permitindo chamar o método da seguinte forma
criar_arquivo_txt()

# Cria um arquivo com o nome informado
criar_arquivo_txt("teste2.txt")
