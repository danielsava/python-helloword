import adivinhacao
import forca


def executar():
    print("")
    print("***********************")
    print("*** Escolha um Jogo ***")
    print("***********************")

    print("\n*** (1) Força  (2) Adivinhação ***")

    jogo = int(input("Qual jogo ?"))

    if jogo == 1:
        print("\nIniciando Jogo de Força", end="\n\n")
        forca.jogar()
    elif jogo == 2:
        print("\nIniciando Jogo de Adivinhação", end="\n\n")
        adivinhacao.jogar()


if __name__ == "__main__":
    executar()
