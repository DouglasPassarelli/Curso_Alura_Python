url = 'https://bytebank.com/cambio?quantidade=100&moedaDestino=Dolar&moedaOrigem=real'

#Url Completa
url_interrogacao = url.find('?')
'''print('URL Completa.')
print(url)
print()'''

#Pegando a Base da nossa URL
'''print('Base da URL.')
url_base = url[:url_interrogacao]
print(url_base)
print()'''

#Pegando os parametros da nosssa URL
print('Parametros da URL.')
url_parametros = url[url_interrogacao+1:]
print(url_parametros)
print()

#Pegando o valor dos parametros da nossa URL
parametro_busca = 'quantidade'
parametro_busca1 = 'moedaOrigem'
parametro_busca2 = 'moedaDestino'
lista_parametros = [parametro_busca, parametro_busca1, parametro_busca2]
for parametros in lista_parametros:
    indice_parametro_busca = url_parametros.find(parametros)
    indice_valor = indice_parametro_busca + len(parametros) + 1
    indice_e_comercial = url_parametros.find('&', indice_valor)
    if indice_e_comercial < 0:
        valor = url_parametros[indice_valor:]
    else:
        valor = url_parametros[indice_valor:indice_e_comercial]
    print(valor)

print('*' * 50)


#Exemplo com a função split()
lista_parametros = url_parametros.split('&')
dict_parametros = {}
for parametros in lista_parametros:
    [nome, valor] = parametros.split('=')
    dict_parametros[nome] = valor

for chave, valor in dict_parametros.items():
    print(f'{chave} = {valor}')

