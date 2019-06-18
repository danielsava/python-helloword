import random


def jogar():

    imprimir_msg_inicializacao()

    gerar_arquivo_palavras()

    palavras = gerar_lista_palavras()
    print("Palavras Secretas: ", palavras, end="\n\n")

    palavra_secreta = escolher_palavra_secreta(palavras)
    print("Palavra Secreta:", palavra_secreta, end="\n\n")

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False

    erros = 0

    while not enforcou and not acertou:

        chute = inserir_chute()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra.strip().lower():
                    print("Encontrei a letra '{}' na posição '{}'".format(letra, index), end="\n\n")
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            desenha_forca(erros)

        print(letras_acertadas, "\n\n")

        enforcou = erros == 7

        if enforcou:
            imprime_mensagem_perdedor(palavra_secreta)

        if erros > 0:
            print("Quantidade de erros: {} de 7".format(erros), end="\n\n")

        if "_" not in letras_acertadas:
            acertou = True
            imprime_mensagem_vencedor()

    print("\n*** Jogo Finalizado ***")


def inserir_chute():
    return input("\nQual a letra: ").lower().strip()


def escolher_palavra_secreta(palavras):
    return palavras[random.randrange(0, len(palavras))]


def gerar_lista_palavras():
    palavras = []
    with open('palavras.txt', 'r') as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip().lower())
    return palavras


def gerar_arquivo_palavras():
    # Somente para criar e preencher o arquivo
    with open('palavras.txt', 'w') as arquivo:
        arquivo.write('siriguela\n')
        arquivo.write('pequi\n')
        arquivo.write('cagaita\n')
        arquivo.write('araticum\n')
        arquivo.write('mangaba\n')
        arquivo.write('buriti\n')
        arquivo.write('baru\n')


def imprimir_msg_inicializacao():
    print("")
    print("**********************************")
    print("*** Bem vindo ao jogo de Força ***")
    print("**********************************", end="\n\n")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


'''

   ******************************************************************************************************************
    Esta função deve SEMPRE ficar no final do arquivo. Python é uma linguagem de script, entao ele deve ler todo o 
    arquivo antes de inicializar o programa.
   * *****************************************************************************************************************
    
'''
if __name__ == "__main__":
    jogar()
