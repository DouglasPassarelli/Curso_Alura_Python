class Filme:

    def __init__(self, nome, ano, duracao):
        self.__nome = nome
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    def mostrar_filme(self):
        print(f'Nome: {vingadores.nome} -- ano: {vingadores.ano}  -- '
              f'duração: {vingadores.duracao} minutos -- likes: {vingadores.likes}')



class Serie:

    def __init__(self, nome, ano, temporadas):
        self.__nome = nome
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    def mostrar_serie(self):
        print(f'Nome: {supernatural.nome} -- ano: {vingadores.ano}  -- '
              f'duração: {supernatural.temporadas} temporadas -- likes: {supernatural.likes}')




vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
vingadores.mostrar_filme()



supernatural = Serie('sobrenatural', 2011, 15)
supernatural.mostrar_serie()
