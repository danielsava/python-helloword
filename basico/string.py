idade = input("Qual sua idade?")

print("Você digitou:", idade)

# Convertendo a string idade no inteiro idade_int
idade_int = int(idade)

print("Idade string concatenada com 2")
print(idade + "2")

print("\n\n")

print("Idade numérica somada com 2")
print(idade_int + 2)

# Formatação de String (interpolação de String)
nome = "Zé"
idade = 30
print("{} tem {} anos".format(nome, idade))

