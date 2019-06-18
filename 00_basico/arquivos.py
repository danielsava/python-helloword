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
arquivo.write("pequi\n")
arquivo.write("siriguela\n")
arquivo.write("cagaita\n")
arquivo.write("araticum\n")

# 'Finaliza' a escrita no arquivo, e fecha o IO com o arquivo
arquivo.close()

# Abre o arquivo e adiciona conteúdo ao arquivo
arquivo = open("palavras.txt", "a")
arquivo.write("\nmaca")
arquivo.write("\nuva")
arquivo.close()

'''
    'with': leitura de arquivos com o 'with'. Com o with não é necessário executar o 'close()', pois dessa forma passa 
                                              a ser responsabilidade do Python fechar o IO.

'''

with open('palavras.txt') as arquivo:
    for linha in arquivo:
        print(linha)


# 'read()' : Lê o conteúdo do arquivo inteiro. Depois da primeira leitura, a segunda vez não retorna nada (ponteiro).
#            Pois o comando 'read()' lê o arquivo inteiro de uma vez, colocando o ponteiro de leitura no final do
#            mesmo. Caso queira ler o arquivo denovo, basta fechar com o 'close()', abri-lo novamente com o 'open()'
arquivo = open('palavaras.txt')
todo_conteudo = arquivo.read()
arquivo.close()

# Lendo o arquivo 'linha' a 'linha' com o 'for'. OBS: O 'print' possui um '\n' embutido, por isso 'pula' uma linha ao
#                                                     ao imprimir.
arquivo = open("palavras.txt", "r")
for linha in arquivo:
    print(linha)
arquivo. close()


# O 'strip()' resolve o problema acima de 'pular uma linha', pois além de ser um 'trim()' ele também o '\n'.
arquivo = open("palavras.txt", "r")
for linha in arquivo:
    print(linha.strip())


# Lendo 'linha a linha' do arquivo com o 'readline()'. É um ponteiro, e cada vez que executa ele lê a próxima linha.
linha = arquivo.readline()
print("Linha 1: ", linha)

linha = arquivo.readline()
print("Linha 2: ", linha)

linha = arquivo.readline()
print("Linha 3: ", linha)


# Cópia de arquivos em modo binário. No caso, gera uma cópia de 'python-logo.png'
logo = open('python-logo.png', 'rb')
data = logo.read()
logo.close()

logo2 = open('python-logo2.png', 'wb')
logo2.write(data)
logo2.close()


