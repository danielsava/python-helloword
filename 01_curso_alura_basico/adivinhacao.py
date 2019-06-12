import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    # Intervalo de 1 à 100
    numero_secreto = random.randrange(1, 101)
    print("\nNúmero Secreto: ", numero_secreto, end="\n\n")

    print("Qual nível de dificuldade ? (1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Escolha um nível de dificuldade: "))

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    print("\nNível Escolhido: ", nivel, end="\n\n")

    rodada = 1

    pontos = 1000

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
            print("\n### Você acertou e faz {} de um máximo de 1.000 pontos ###".format(pontos))
            break
        else:
            if maior:
                print("O chute foi maior do que o número secreto")
            elif menor:
                print("O chute foi menor do que o número secreto")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        print("\n")

    print("\n*** Jogo Finalizado ***")


# Para ser executado somente quando o script for 'chamado' diretamente
if __name__ == "__main__":
    jogar()
