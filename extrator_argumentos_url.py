class ExtratorArgumentoUrl:

    def __init__(self, url):
        if self.url_valida(url):
            self.url = url.lower()
        else:
            raise LookupError("Url Inválida")

    def __len__(self):
        return len(self.url)


    # Utilizado pelo 'print'. Cria uma representação em String da classe
    def __str__(self):
        moedaOrigem, moedaDestino = self.extrair_argumentos()
        return f"MoedaOrigem: {moedaOrigem}, MoedaDestino: {moedaDestino}, Valor: R$ {self.extrair_valor()}"


    def __eq__(self, other):
        if not other:
            return False

        if isinstance(other, ExtratorArgumentoUrl):
            return self.url == other.url
        else:
            return False




    @staticmethod
    def url_valida(url):
        if url and url.startswith("https://bytebank.com"):
            return True
        else:
            return False

    def extrair_argumentos(self):

        busca_moeda_origem = "moedaorigem=".lower()

        busca_moeda_destino = "moedadestino=".lower()

        indice_inicial_moeda_origem = self.encontrar_indice_inicial(busca_moeda_origem)
        indice_final_moeda_origem = self.url.find("&")
        moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

        if moeda_origem == "moedadestino":
            self.trocar_moeda_origem()

            indice_inicial_moeda_origem = self.encontrar_indice_inicial(busca_moeda_origem)
            indice_final_moeda_origem = self.url.find("&")
            moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

        indice_inicial_moeda_destino = self.encontrar_indice_inicial(busca_moeda_destino)
        indice_final_moeda_destino = self.url.find("&valor")
        moeda_destino = self.url[indice_inicial_moeda_destino:indice_final_moeda_destino]

        valor = self.extrair_valor()

        return moeda_origem, moeda_destino, valor

    def encontrar_indice_inicial(self, moeda_buscada):
        return self.url.find(moeda_buscada) + len(moeda_buscada)

    def trocar_moeda_origem(self):
        self.url = self.url.replace("moedadestino", "real", 1)

    def extrair_valor(self):
        busca_valor = "valor="
        indice_inicial_valor = self.encontrar_indice_inicial(busca_valor)
        valor = self.url[indice_inicial_valor:]
        return valor
