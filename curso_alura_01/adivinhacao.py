print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_tentativas = 3
rodada = 1

jogo_finalizado = False

while rodada <= total_tentativas:

    print("Tentativa {} de {}".format(rodada, total_tentativas))

    chute_str = input("Digite o seu número: ")
    print("Você digitou", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou")
        jogo_finalizado = True
    else:
        if maior:
            print("O chute foi maior do que o número secreto")
        elif menor:
            print("O chute foi menor do que o número secreto")

    print("\n")

    rodada = rodada + 1

    if jogo_finalizado or rodada > total_tentativas:
        print("*** Jogo Finalizado ***")
        break

