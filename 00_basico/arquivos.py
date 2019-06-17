"""
    Leitura e Escrita de arquivos em Python




    'open(arg1, ar2)'
        - arg1: nome do arquivo
        - arg2:
            "w": CRIA um arquivo em modo ESCRITA. Caso exista um arquivo de mesmo nome, ele será sobrescrito.
            "a": ABRE um arquivo em modo ESCRITA e ADICIONA conteúdo no arquivo
            "r": ABRE um arquivo em modo LEITURA (MODO DEFAULT, caso não seja informado o 'arg2')
            "b": Modo BINARIO. Deve ser informado caso deseje ler um arquivo em binário, como por exemplo uma imagem.
                - logo = open('python-logo.png', 'rb') : abre a logo em binário no modo 'somente leitura'

    Class: '_io.TxtIOWrapper'

"""

# Cria um arquivo, em branco, 'palavras.txt'
arquivo = open("palavras.txt", "w")

# Escreve no arquivo
arquivo.write("banana")

# 'Finaliza' a escrita no arquivo, e fecha o IO com o arquivo
arquivo.close()

# Abre o arquivo e adiciona conteúdo ao arquivo
arquivo = open("palavras.txt", "a")
arquivo.write("\nmaca")
arquivo.write("\nuva")
arquivo.close()


# 'read()' : Lê o conteúdo do arquivo inteiro. OBS: depois da primeira leitura, a segunda vez não retorna nada.
todo_conteudo = arquivo.read()


# Lendo o arquivo 'linha' a 'linha' com o 'for'
arquivo = open("palavras.txt", "r")
for linha in arquivo:
    print(linha)


# Utilizando o 'readline()'





# Cópia de arquivos em modo binário. No caso, gera uma cópia de 'python-logo.png'
logo = open('python-logo.png', 'rb')
data = logo.read()
logo.close()

logo2 = open('python-logo2.png', 'wb')
logo2.write(data)
logo2.close()
