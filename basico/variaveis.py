
"""
    Padrão para nome de variáveis: O nome de variáveis em Python segue o padrão "Snake_Case"
"""

idade_esposa = 20
perfil_vip = 'Daniel Sava'
recibos_em_atraso = 30


"""
    Definindo Variáveis
"""

# Definindo Variáveis
pais = "Itália"


"""
    String : 'str'    
"""
tipo_string = "nome"
print("String: ", type(tipo_string))

"""
    Inteiro : 'int'    
"""
quantidade = 4
print("inteiro: ", type(quantidade))


"""
    Booleano : 'bool'    
"""
idade = 20
tipo_booleano = idade > 18
print("Booleano: ", type(tipo_booleano))


"""
    Float : 'float'    
"""
tipo_float = 19.00
print("Float: ", type(tipo_float))

"""
    Comparando Variáveis
"""
var1 = "nome"
var2 = 19
var3 = 'nome'
var4 = 20
var5 = 19

if var1 == var3:
    print("**** iguais ****")


"""
    Conversão de Variáveis
"""

cpf = "00122315170"

print("'cpf' String: ", cpf)

# Convertendo para Inteiro
print("'cpf' Inteiro: ", int(cpf))


# ERRO
idade1 = 10
idade2 = "20"
print(idade1 + idade2)

