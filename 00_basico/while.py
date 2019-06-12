

"""
    # 'break':  quebra o Laço, tanto no 'while' quanto no 'for'
    # 'continua': pula para o próximo item do laço

"""

# Exemplo 1
qtd = int(input("Digite a quantidade: "))

num = 0

while num <= qtd:
    print(num)
    num = num + 1
    if num == 10:
        break


# Exemplo 2

var1 = True
var2 = True

c1 = 0

while var1 and var2:
    print("Contador:", c1)
    c1 = c1 + 1
    if c1 >= 15:
        var1 = False





