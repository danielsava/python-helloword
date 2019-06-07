print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_tentativas = 3
rodada = 1

for rodada in range(1, total_tentativas + 1):

    print("Tentativa {} de {}".format(rodada, total_tentativas))

    chute_str = input("Digite o seu número entre 1 e 100: ")
    print("Você digitou", chute_str)
    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print("*** Alerta : Você deve digitar um número entre 1 e 100 ***", end="\n\n")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou")
        break
    else:
        if maior:
            print("O chute foi maior do que o número secreto")
        elif menor:
            print("O chute foi menor do que o número secreto")

    print("\n")

print("*** Jogo Finalizado ***")

