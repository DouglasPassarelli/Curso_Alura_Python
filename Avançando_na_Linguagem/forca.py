def jogar():
    def menu(msg, tam=0):
        tam = len(msg)
        print('*' * tam)
        print(msg)
        print('*' * tam)

    def letras_disponiveis(list, indece):
        """print(*list)"""
        i = list.index(indece)
        list[i] = '*'
        return list




    menu('Bem vindo ao jogo da forca!')

    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
              'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Z']
    palavra_secreta = "banana"
    letras_acertadas = ['_', '_', '_', '_', '_', '_']
    acertou = False
    enforcou = False

    """print(*letras_disponiveis)"""
    print('Letras disponiveis:', *letras)
    print(*letras_acertadas)
    while not acertou and not enforcou:
        chute = input('Qual a letra? ').strip().upper()
        disponiveis = letras_disponiveis(letras, chute)
        print('Letras disponiveis:', *disponiveis)
        for index, letra in enumerate(palavra_secreta):
            if chute == letra.upper():
                letras_acertadas[index] = letra

        print(*letras_acertadas)

    print('Fim do Jogo')


if __name__ == "__main__":
    jogar()