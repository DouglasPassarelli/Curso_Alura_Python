import forca
import adivinhacao


def escolhe_jogo():
    def menu(msg, tam=0):
        tam = len(msg)
        print('*' * tam)
        print(msg)
        print('*' * tam)


    menu('Bem vindo a Sala de Jogos!')

    print('Escolha uma opção para iniciar')
    print('(1) Forca   (2) Adivinhação')
    jogo = int(input('Qual deseja jogar: '))

    if jogo == 1:
        print('Iniciando o Jogo da Forca...')
        forca.jogar()
    elif jogo == 2:
        print('Iniciando o Jogo da Adivinhação...')
        adivinhacao.jogar()
    print('Saindo da sala de jogos...')


if __name__ == "__main__":
    escolhe_jogo()
