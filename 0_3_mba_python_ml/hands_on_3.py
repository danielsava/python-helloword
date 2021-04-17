import traceback

# Gerando erro de teste
try:
    y = 10 / x
except:
    print('falhou')
    traceback.print_exc()


# Definindo anotação/decorator @show_exception
def show_exception(func):
    def wrapper():
        try:
            func()
        except:
            print('Erro:')
            traceback.print_exc()
    return wrapper  


# Usando a anotação
@show_exception
def gerar_erro():
     return 10 / x

# 
gerar_erro()