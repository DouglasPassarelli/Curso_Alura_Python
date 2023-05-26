def jogar():
    def linhas(tam=27):
        print('*' * tam)


    def menu(msg, tam=0):
        tam = len(msg)
        print('*' * tam)
        print(msg)
        print('*' * tam)

    def letras_disponiveis(list, indece):
        if indece in list:
            i = list.index(indece)
            list[i] = '*'
            print(f'Letras Disponiveis:', *list)
        else:
            print('Esta letra ja foi selecionada, Por favor digite outra!')
            print(f'Letras Disponiveis:', *list)

    menu('Bem vindo ao jogo da forca!')

    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
              'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Z']
    palavra_secreta = "maça".upper()
    letras_acertadas = ['_' for letra in palavra_secreta]
    acertou = False
    enforcou = False
    tentativa = 6
    rodadas = 0

    print(f'A Palavra chave tem {len(palavra_secreta)} letras.')
    print('Letras disponiveis:', *letras)
    print('Palavra-Chave:', *letras_acertadas)
    linhas()


    while not acertou and not enforcou:
        chute = input('Qual a letra? ').strip().upper()
        letras_disponiveis(letras, chute)
        if chute in palavra_secreta:
            print('Voce acertou!!!')
            for index, letra in enumerate(palavra_secreta):
                if chute == letra.upper():
                    letras_acertadas[index] = letra
            print(f'Ainda restam {letras_acertadas.count("_")} letras')
        else:
            tentativa -= 1
            print(f'Voce errou, ainda restam {tentativa} tentativas!')

        print('Palavra-chave:', *letras_acertadas)
        rodadas += 1
        linhas()
        acertou = '_' not in letras_acertadas
        enforcou = tentativa == 0

    if acertou:
        print('Parabens voce ganhou o jogo da forca.')
        print(f'Voce ganhou com {rodadas} rodadas')
        print(f'Palavra chave: {palavra_secreta} ')
    else:
        print('Voce perdeu, Mais sorte da proxima veiz!')
        print(f'A palavra chave era {palavra_secreta}')
        print('Ate a proxima!')


    print('Fim do Jogo')


if __name__ == "__main__":
    jogar()