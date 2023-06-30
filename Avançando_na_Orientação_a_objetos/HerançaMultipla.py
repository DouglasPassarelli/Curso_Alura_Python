"""Exemplo mostrado na Aula sobre Herança Multipla"""



class Funcionario:
    def __init__(self, nome):
        self.nome = nome


    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

#classe mixin
class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'


class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Senior(Caelum, Alura, Hipster):
    pass

print('Funcionario Junior')
jose = Junior('junior')
jose.mostrar_tarefas()
jose.busca_perguntas_sem_resposta()
print('*' * 20)
print('\n')

print('Funcionario Pleno')
luan = Pleno('Luan')
luan.mostrar_tarefas()
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()
print('*' * 20)
print('\n')

print('Funcionario Senior')
douglas = Senior('douglas')
print(douglas)
douglas.mostrar_tarefas()
douglas.busca_perguntas_sem_resposta()
douglas.busca_cursos_do_mes()
print('*' * 20)


"""MRO
PLENO > ALURA > FUNCIONARIO > CAELUM > FUNCIONARIO

No nosso caso, em vez de Funcionario, Caelum é que foi acessado, pois a parte da 
remoção da duplicidade verifica se Funcionario é "uma boa cabeça" (good head). 
Caso positivo, quer dizer que poderemos mantê-la. Como o primeiro Funcionario não é uma good head, 
iremos removê-la:

Pleno > Alura > Caelum > Funcionario"""