"""
    'String'
"""

#
idade = "28"
print("Você digitou:", idade)

# Tamanho da String
print(len(idade))

"""
    String também sao Listas:
        - Por isso vários métodos das listas tb são aplicadas às Strings
"""
print(max(idade))
print(min(idade))
print(idade[1])


"""
    'Conversão'
"""
idade_int = int(idade)


'''
    Interpolação com String
'''

nome = "Zé"
idade = 30
print("{} tem {} anos".format(nome, idade))

# Informando a localização da interpolação
print("Tentativa {1} de {0}".format(3, 10))


'''
    Interpolação com Variáveis
'''

nome = "Daniel"
sobrenome = "Sava"

print(f"Meu nome é {nome} {sobrenome}")
print(f"Meu nome é {nome.upper()}")


'''
    Interpolação e formatação com Inteiro
'''

print("R$ {:7d}".format(4))

# Preenche com zeros
print("R$ {:07d}".format(4))

print("Data {:02d}/{:02d}".format(19, 2))


'''
    # Interpolação e formatação com Float
'''

print("R$ {}".format(1.59))
print("R$ {:f}".format(1.59))
print("R$ {:.2f}").format(1.59)
print("R$ {:.2f}").format(1.5)
print("R$ {:.2f}").format(1234.5)

# Coloca os espaços, antes do ponto, até completar 7 casas
print("R$ {:7.2f}").format(4.5)

# Preenche com zeros
print("R$ {:07.2f}").format(4.5)
print("R$ {:08.3f}").format(4.5)

'''
    'Pesquisar' dentro das String´s
'''

# 'find': retorna a posição, dentro da string, para a primeira ocorrência do caracter informado
palavra = "banana"
print(palavra.find("b"))


# 'for': Usando iteração
for letra in palavra:
    print(letra)


'''
    'Capitalize' 
'''
palavra_capitalizada = palavra.capitalize()
print(palavra_capitalizada)


'''
    'strip': é o 'trim' do Python 
'''
print("   teste   ".strip())