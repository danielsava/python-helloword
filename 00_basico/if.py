idade = int(input("Digite a idade:"))

if idade < 16:
    print("Nao pode votar")
else: 
    print("Pode votar")


# Com o uso de paranteses (recomendado pelas boas práticas em Python)

if idade < 16:
    print("Não pode votar")
else:
    print("Pode votar")


# Uso do 'ELIF'

if idade >= 18:
    print("Já tem 18 anos")
else:
    if idade >= 16:
        print("No máximo em 2 anos você terá 18 anos")
    elif 10 < idade < 16 and idade != 0:
        print("Falta pouco para os 18 anos")
    elif idade <= 10:
        print("Você não completou nem 10 anos ainda")

