"""

    # Padrão para nome de variáveis:

        - O nome de variáveis em Python segue o padrão "Snake_Case",
        Diferente do Java e outras linguagens que seguem o padrão "CamelCase"

"""

idade_esposa = 20
perfil_vip = 'Daniel Sava'
recibos_em_atraso = 30


# Definindo Variáveis
pais = "Itália"

# String
tipoVarPais = type(pais)                        # 'type' retorna uma classe contendo o tipo da variável informada
print("Variável 'pais': " + str(tipoVarPais))

# Int
quantidade = 4
tipoVarQuantidade = type(quantidade)
print("Variável 'quantidade': " + str(tipoVarQuantidade))


#
print(pais, "ganhou", quantidade, "títulos mundiais")