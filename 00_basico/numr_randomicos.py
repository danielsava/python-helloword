import random

numr_rand = random.random()
print(numr_rand)

numr_rand_1 = random.random() * 100
print(numr_rand_1)

# Inteiros : com a função 'round' ele arredonda o número
numr_rand_inteiro = round(numr_rand_1)
print(numr_rand_inteiro)

# Inteiros : com a função 'int' ele transforma 'float' em int
numr_rand_inteiro2 = int(numr_rand_1)
print(numr_rand_inteiro2)

# gera um número entre o 5 e o 8
numr3 = random.uniform(5, 8)
print(numr3)
