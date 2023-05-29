def jogar():

    def linhas(tam=27):
        print('*' * tam)

    def menu_jogo(msg, palavra, disponiveis, acertadas, tam=0):
        tam = len(msg)
        print('*' * tam)
        print(msg)
        print('*' * tam)
        print(f'A Palavra chave tem {len(palavra)} letras.')
        print('Letras disponiveis:', *disponiveis)
        print('Palavra-Chave:', *acertadas)
        linhas()

    def teste_letras_disponiveis(palpite, disponiveis):
        clone = disponiveis.copy()
        for index, letra in enumerate(disponiveis):
            if palpite == letra.upper():
                clone[index] = '*'
        return clone

    def teste_jogo(palavra, palpite, acertos):
        for index, letra in enumerate(palavra):
            if palpite == letra.upper():
                letras_acertadas[index] = letra
        return acertos

    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
              'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Z', 'Ç']
    palavra_secreta = "maça".upper()
    letras_acertadas = ['_' for letra in palavra_secreta]
    acertou = False
    enforcou = False
    tentativa = 6
    rodadas = 0

    menu_jogo('Bem vindo ao jogo da forca!', palavra_secreta, letras, letras_acertadas)

    while not acertou and not enforcou:
        chute = input('Qual a letra? ').strip().upper()
        comparacao = chute
        if chute in palavra_secreta and chute in letras:
            print('Voce acertou!!!')
            letras_acertadas = teste_jogo(palavra_secreta, chute, letras_acertadas)
            print(f'Ainda restam {letras_acertadas.count("_")} letra(s)')
        else:
            if comparacao not in letras:
                print('Esta letra não esta disponivel pois ja foi escolhida, Por favor digite outra!')
            else:
                tentativa -= 1
                print(f'Voce errou, ainda restam {tentativa} tentativas!')

        letras = teste_letras_disponiveis(chute, letras)
        print('Palavra-chave:', *letras_acertadas)
        print('Letras disponiveis:', *letras)
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
