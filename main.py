from extrator_argumentos_url import ExtratorArgumentoUrl

url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=700"

argumentos_url = ExtratorArgumentoUrl(url)

moeda_origem, moeda_destino, valor = argumentos_url.extrair_argumentos()

print("Moeda Origem: ", moeda_origem.capitalize())
print("Moeda Destino: ", moeda_destino.capitalize())
print("Valor: ", f"R$ {valor}")
