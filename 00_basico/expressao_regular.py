"""
    Expressões Regulares
     - Necessário importar a biblioteca 're'
"""

import re

telefone1 = "Meu número é 1234-1234"
telefone2 = "Fale comigo em 1234-1234 esse é meu telefone"
telefone3 = "1234-1234 é o meu celular"
telefone4 = "Entao , meu contato e o 99543-1254. Mas posso atender també no 9876-1234"

# Configura os caracteres que deseja encontrar em cada 'sessão'(delimitada pelos colchetes)
padrao_telefone = "[123456789][123456789][123456789][123456789]-[123456789][123456789][123456789][123456789]"

# Mesmo padrão acima
padrao_telefone2 = "[0-9][0-9][0-9][0-9][-][0-9][0-9][0-9][0-9]"

# Mesmo padrão acima
padrao_telefone3 = "[0-9]{4}[-][0-9]{4}"

# Configura intervalo de 4 ou 5 conjuntos de '0-9' ('99981-6300' e '9981-6300' são válidos)
padrao_telefone4 = "[0-9]{4,5}[-][0-9]{4}"

# Não obrigatório o uso do hifen "-"
padrao_telefone5 = "[0-9]{4,5}[-]*[0-9]{4}"

retorno = re.findall(padrao_telefone4, telefone4)
print(retorno)



''' 
    'search': Retorna, dentro da string informada, alguma ocorrência com o padrão informado
'''

retorno = re.search(padrao_telefone, telefone1)
print(retorno.group())
