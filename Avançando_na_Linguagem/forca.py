def jogar():
    def menu(msg, tam=0):
        tam = len(msg)
        print('*' * tam)
        print(msg)
        print('*' * tam)


    menu('Bem vindo ao jogo da forca!')

    palavra_secreta = "banana"
    acertou = False
    enforcou = False

    while not acertou and not enforcou:
        chute = input('Qual a letra? ').strip().upper()

        for index, letra in enumerate(palavra_secreta):
            if chute == letra.upper():
                print(f'Encontrei a letra {chute} na posição {index}')

        print("jogando...")


if __name__ == "__main__":
    jogar()