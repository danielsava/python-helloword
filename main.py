from extrator_argumentos_url import ExtratorArgumentoUrl

url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=700"
url2 = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=euro&valor=600"

ex_url_1 = ExtratorArgumentoUrl(url)
ex_url_2 = ExtratorArgumentoUrl(url2)

moeda_origem, moeda_destino, valor = ex_url_1.extrair_argumentos()

print("Moeda Origem: ", moeda_origem.capitalize())
print("Moeda Destino: ", moeda_destino.capitalize())
print("Valor: ", f"R$ {valor}")

print("Da mesma classe: ", ex_url_1 == ex_url_2)
