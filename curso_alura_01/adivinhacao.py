print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")
print("Você digitou", chute_str)
chute = int()


if numero_secreto == chute:
    print("Você acertou")
else:
    print("Você errou")


chute = input("Digite, novamente, seu número: ")

print("Você digitou", chute)

if numero_secreto == int(chute):
    print("Você acertou")
else:
    print("Você errou")