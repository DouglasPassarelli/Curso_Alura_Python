class Programa:

    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome.title()

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        print('Um like foi adicionado!')
        self._likes += 1

    def __str__(self):
        resultado = ''
        conteudo = {'Nome': self.nome,
                    'Ano': self.ano,
                    'Likes': self.likes}
        for chave, valor in conteudo.items():
            resultado += f'{chave}: {valor}\n'
        return resultado


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        resultado = ''
        conteudo = {'Nome': self.nome,
                    'Ano': self.ano,
                    'Duração': f"{self.duracao} minutos",
                    'Likes': self.likes}
        for chave, valor in conteudo.items():
            resultado += f'{chave}: {valor}\n'
        return resultado


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        resultado = ''
        conteudo = {'Nome': self.nome,
                    'Ano': self.ano,
                    'Duração': f"{self.temporadas} temporadas",
                    'Likes': self.likes}
        for chave, valor in conteudo.items():
            resultado += f'{chave}: {valor}\n'
        return resultado


class Playlist(list):

    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)


demon_slayer = Filme('Kimetsu no yaba', 2019, 160)
demon_slayer.dar_likes()
demon_slayer.dar_likes()

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()

homen_Aranha = Filme('Homem Aranha', 2021, 160)


supernatural = Serie('sobrenatural', 2011, 15)
supernatural.dar_likes()

the_witcher = Serie('The witcher', 2016, 3)
the_witcher.dar_likes()
the_witcher.dar_likes()
the_witcher.dar_likes()

filmes_e_series = [vingadores, supernatural, demon_slayer, the_witcher]
playlist_melhores_de_todos = Playlist('Melhores de todos', filmes_e_series)

'''for programa in playlist_melhores_de_todos:
    print(programa, end='')'''

print(f'Tamanho da playlist: {len(playlist_melhores_de_todos)}')
playlist_melhores_de_todos.append(homen_Aranha)


for programa in playlist_melhores_de_todos:
    print(programa, end='')