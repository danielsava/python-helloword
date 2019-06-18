import random


def jogar():
    print("")
    print("**********************************")
    print("*** Bem vindo ao jogo de Força ***")
    print("**********************************", end="\n\n")

    # Somente para criar e preencher o arquivo
    with open('palavras.txt', 'w') as arquivo:
        arquivo.write('siriguela\n')
        arquivo.write('pequi\n')
        arquivo.write('cagaita\n')
        arquivo.write('araticum\n')
        arquivo.write('mangaba\n')
        arquivo.write('buriti\n')
        arquivo.write('baru\n')

    # Arquivo modo leitura
    palavras = []
    with open('palavras.txt', 'r') as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip().lower())

    #
    print("Palavras Secretas: ", palavras, end="\n\n")

    # Escolhendo uma Palavra
    palavra_secreta = palavras[random.randrange(0, len(palavras))]

    print("Palavra Secreta:", palavra_secreta, end="\n\n")

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False

    erros = 0

    while not enforcou and not acertou:

        chute = input("\nQual a letra: ").lower().strip()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra.strip().lower():
                    print("Encontrei a letra '{}' na posição '{}'".format(letra, index), end="\n\n")
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        print(letras_acertadas, "\n\n")

        enforcou = erros == 6

        if erros > 0:
            print("Quantidade de erros: {} de 6".format(erros), end="\n\n")

        if "_" not in letras_acertadas:
            print("\n*** Você acertou a palavra ****")
            acertou = True

    print("\n*** Jogo Finalizado ***")


# Inicio Execução
if __name__ == "__main__":
    jogar()
