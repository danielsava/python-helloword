
"""
   No Python são consideradas sequências (coleções);

    - 'list'

    - 'tuple': Imutável

    - 'range': Imutável

    - 'string': Imutável
        String é uma sequência de caracter

    - 'dictionary'
        Lista Chave Valor


"""

"""
    'List'
     - O único tipo de sequência no Python que é mutável.
"""

#
valores = ["a", "b", "c"]
print(type(valores))

"""
    Formas de INICIALIZAR
"""

# Inicializa a lista com o caracter '"_"' para cada letra da string 'palavra'
palavra = "banana"
letras_acertadas = ["_" for letra in palavra]

# Inicializa 'lista2' com cada palavra de 'frutas' convertidas para maiúsculas
frutas = ["maça", "banana", "laranja", "melancia"]
lista2 = [fruta.upper() for fruta in frutas]

# Inicializa a coleção com o quadrado da lista de 'inteiros'
inteiros = [1, 2, 3, 4, 5, 6, 7, 8]
quadrados = [i*i for i in inteiros]

# Com CONDICIONAL IF, para criar uma lista somente com números pares
numr_pares = [n for n in inteiros if n % 2 == 0]


"""
    Index: Posição do elemento dentro da coleção
"""
print(valores[0])

# Inserindo valores
valores.append("d")

# Inserindo valores numa posição específica
valores[1] = "e"

# Verifica se existe o valor dentro da lista
existe = "a" in valores
print(existe)

# Valores Maiores ou Menores
valores = [1, 2, 3, 4]
valor_minino = min(valores)
print("Valor mínimo da Lista:", valor_minino)

valor_max = max(valores)
print("Valor max da Lista:", valor_max)

# Tamanho da List
print(len(valores))

# Adiciona itens na Lista
valores.append(10)
print(valores)

# Remove itens na Lista
valores.remove(3)
print(valores)

# Retorna e retira o último elemento da Lista
ultimo_item = valores.pop()
print(ultimo_item)

# Inverte a Lista
valores.reverse()
print(valores)

# Limpa toda a Lista
valores.clear()
print(valores)

# Quantidade de ocorrências dentro da Lista
print(valores.count(10))



"""
    'set'
     - Mesmo conceito do Java, quando comparamos List com Set. Ou seja, o Set não permite valores duplicados
     - Set não possui índice.
"""

set1 = {"Daniel", "Leonardo", "Guilherme"}

# Adiciona o "Luciana"
set1.add("Luciana")

# Não altera a sequencia porque já existe o valor
set1.add("Daniel")

set1.add("teste")

# Remove o valor informado, caso exista. Caso não existe, é lançado um erro.
set1.remove("teste")



"""
    'tuple'
        - As tuplas, diferente da lista, não mudam. Não podem ser alteradas, portanto são IMUTÁVEIS.
"""

tupla = 12, 3134, 434, "a", "teste"
print(type(tupla))

for item in tupla:
    print(item)

existe = 3134 in tupla
print(existe)

exite = "a" in tupla
print(existe)



"""
    'range'
        - Aceita somente valores do tipo 'Integer', além de ser imutável
"""
serie = range(0, 10)

print(type(serie))

for i in serie:
    print(i)



"""
    Convertendo Coleções
        
"""
list1 = ["a" "b", "c", "d"]
list1_tuple = tuple(list1)

tuple1 = "a", "b", "c", "d"
tuple1_list = list(tuple1)



"""
    Matriz: Sequências dentro de Sequências
    
"""

instrutor1 = ("Nico", 39)
instrutor2 = ("Flávio", 37)

instrutores = [instrutor1, instrutor2]

idade_instrutor1 = instrutores[0][1]
print(idade_instrutor1)



"""
    'dict': 
        - É o dicionário. São as sequências 'Chave / Valor' no Python

"""

instrutores = {'Nico': 39, 'Flávio': 37, 'Marcos': 30}

print(type(instrutores))

# Imprimindo a idade de Nico
print(instrutores['Nico'])






