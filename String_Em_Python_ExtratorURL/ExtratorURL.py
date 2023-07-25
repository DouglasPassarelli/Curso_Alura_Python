import re

class ExtratorURL:

    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def __str__(self):
         return f'Url Completa: {self.url}' + '\n' + f'Url Base: {self.get_base_url()}' + '\n' + f'Url parametros: {self.get_parametros_url()} '

    def __len__(self):
        return len(self.url)

    def __eq__(self, other):
        return self.url == other.url

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
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?(/cambio)')
        busca = padrao_url.match(self.url)
        if not busca:
            raise ValueError('URL Invalida!')


    '''def validacao_url_base(self):
        Validação usando os metodos endswith e startswith
        if not str.endswith(self.get_base_url(), 'cambio'):
            raise ValueError('Pagina na URL nao encontrada!')
        elif not str.startswith(self.get_base_url(), 'https'):
            raise ValueError('HTTPS nao encontrado!')'''

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


'''
Desafio Passado no Curso
Modifique o nosso projeto, 
levando em conta o valor do dólar em real 
(por exemplo: DOLAR = 5.50), para, sabendo o valor do dólar em real 
(por exemplo: DOLAR = 5.50), ler da URL os 3 parâmetros (
origem, destino e quantidade) e imprimir na tela o valor da conversão.

'''


class Conversor_moedas:

    def __init__(self, valor_dolar, quantidade_real):
        self._valor_dolar = float(valor_dolar)
        self._quantidade_real = float(quantidade_real)

    def __str__(self):
        return f'Valor Dolar: {self.valor_dolar}' + '\n' + f'Quantidade de moedas em Real: {self.quantidade_real}'

    @property
    def valor_dolar(self):
        return f'U${float(self._valor_dolar):.2f}'

    @valor_dolar.setter
    def valor_dolar(self, novo_valor):
        self._valor_dolar = novo_valor


    @property
    def quantidade_real(self):
        return f'R${float(self._quantidade_real):.2f}'

    @quantidade_real.setter
    def quantidade_real(self, novo_valor):
        self._quantidade_real = novo_valor

    def conversor(self):
        result = self._quantidade_real * self._valor_dolar
        return result

    def mostrar_conversao(self):
        print(f'Conversão de R${self._quantidade_real:.2f} para dolar ficara em um total de R${self.conversor():.2f}!! \n'
              f'Sabendo que o valor do Dolar e de U${self._valor_dolar:.2f}')


url = ExtratorURL('https://bytebank.com/cambio?quantidade=100&moedaDestino=Dolar&moedaOrigem=real')
url1 = ExtratorURL('https://bytebank.com/cambio?quantidade=100&moedaDestino=Dolar&moedaOrigem=real')
conversao1 = Conversor_moedas(5.50, url.valores_parametros('quantidade'))
#url = ExtratorURL('   ')
print(url)
print(f'Tamanho URL:{len(url)}')
print(url.get_base_url())
print(url.get_parametros_url())
print(url.valores_parametros('quantidade'))
print(f'Comparando dois objetos (url e url1): {url == url1}')
print(conversao1)
conversao1.mostrar_conversao()
