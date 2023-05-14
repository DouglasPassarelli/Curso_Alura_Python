def jogar():
    def menu(msg, tam=0):
        tam = len(msg)
        print('*' * tam)
        print(msg)
        print('*' * tam)


    menu('Bem vindo ao jogo da forca!')


if __name__ == "__main__":
    jogar()