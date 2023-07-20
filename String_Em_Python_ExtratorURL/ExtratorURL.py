class ExtratorURL:

    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def __str__(self):
        return f'Url Completa: {self.url}'

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError('A URL esta vazia!')
        self.validacao_url_base()

    def validacao_url_base(self):
        if not str.endswith(self.get_base_url(), 'cambio'):
            raise ValueError('Pagina na URL nao encontrada!')
        elif not str.startswith(self.get_base_url(), 'https'):
            raise ValueError('HTTPS nao encontrado!')

    def get_base_url(self):
        url_interrogacao = self.url.find('?')
        url_base = self.url[:url_interrogacao]
        return url_base

    def get_parametros_url(self):
        url_interrogacao = self.url.find('?')
        url_parametros = self.url[url_interrogacao+1:]
        return url_parametros

    def valores_parametros(self, parametro):
        indice_parametro_busca = self.get_parametros_url().find(parametro)
        indice_valor = indice_parametro_busca + len(parametro) + 1
        indice_e_comercial = self.get_parametros_url().find('&', indice_valor)
        if indice_e_comercial < 0:
            valor = self.get_parametros_url()[indice_valor:]
        else:
            valor = self.get_parametros_url()[indice_valor:indice_e_comercial]
        return valor


url = ExtratorURL('https//bytebank.com/cambio?quantidade=100&moedaDestino=Dolar&moedaOrigem=real')
#url = ExtratorURL('   ')
print(url)
print(url.get_base_url())
print(url.get_parametros_url())
print(url.valores_parametros('moedaOrigem'))