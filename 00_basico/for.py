
# For 'default'
usuarios = ['Maria', 'Jose', 'Carlos']

for u in usuarios:
    print("Usuários", u)

for numrs in [1, 2, 3, 4, 5]:
    print(numrs)

# Uso do 'range'
numeros = range(2, 10, 3)

for n in numeros:
    print("Números", n)

#
for rodada in range(1, 10):
    print("Rodada: ", rodada)


# Uso do 'range' com 'step'
for rodada in range(1, 10, 2):
    print("Rodada Step: ", rodada)

for contador in range(1, 11, 3):
    print(contador)

# Se fosse fazer o 'range' acima com o 'while' ficaria
contador = 1
while contador <= 10:
    print(contador)
    contador = contador + 3

# Iterando sobre uma String, imprimindo cada letra da String
for letra in "teste":
    print(letra)

