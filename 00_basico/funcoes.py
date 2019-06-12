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

