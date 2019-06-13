def jogar():

    print("**********************************")
    print("*** Bem vindo ao jogo de Força ***")
    print("**********************************", end="\n\n")

    palavra_secreta = "banana"

    print("Palavra Secreta:", palavra_secreta, end="\n\n")

    letras_acertadas = []

    for l in palavra_secreta:
        letras_acertadas.append("_")

    enforcou = False
    acertou = False

    while not enforcou and not acertou:

        chute = input("Qual a letra: ").lower().strip()

        index = 0

        for letra in palavra_secreta:
            if chute == letra.lower().strip():
                print("Encontrei a letra '{}' na posição '{}'".format(letra, index), end="\n\n")
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas, "\n\n")

        if letras_acertadas.count("_") == 0:
            print("*** Você acertou a palavra ****")
            acertou = True

    print("*** Jogo Finalizado ***")


# Inicio Execução
if __name__ == "__main__":
    jogar()
