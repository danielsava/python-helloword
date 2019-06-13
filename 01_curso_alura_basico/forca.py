def jogar():
    print("**********************************")
    print("*** Bem vindo ao jogo de Força ***")
    print("**********************************", end="\n\n")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while not enforcou and not acertou:

        chute = input("Qual a letra: ").lower().strip()

        index = 0

        for letra in palavra_secreta:
            if chute == letra.lower().strip():
                print("Encontrei a letra '{}' na posição '{}'".format(letra, index))
                acertou = True
            index = index + 1

    print("\n*** Jogo Finalizado ***")


# Inicio Execução
if __name__ == "__main__":
    jogar()
