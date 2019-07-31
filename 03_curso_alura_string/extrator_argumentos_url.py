class extrator_argumentos_url:


    def __init__(self, url):
        if self.url_valida(url):
            self.url = url
        else:
            raise LookupError("Url Inválida")


    def url_valida(self, url):
        if url:
            return True
        else:
            return False

