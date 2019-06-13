"""
    'List'
"""

valores = ["a", "b", "c"]
print(type(valores))


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



"""
    'tuple'
"""

tupla = 12, 3134, 434, "a", "teste"
print(type(tupla))

for item in tupla:
    print(item)

existe = 3134 in tupla
print(existe)

