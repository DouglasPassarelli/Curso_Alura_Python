
from random import randrange


def jogar():

    arquivo = 'palavras.txt'
    if not arqexiste(arquivo):
        arquivo = criararq(arquivo)

    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
              'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    palavra_secreta = gerando_palavra_secreta(arquivo)
    letras_acertadas = ['_' for letra in palavra_secreta]
    acertou = False
    enforcou = False
    tentativa = 0
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
                tentativa += 1
                desenha_forca(tentativa)

        letras = teste_letras_disponiveis(chute, letras)
        print('Palavra-chave:', *letras_acertadas)
        print('Letras disponiveis:', *letras)
        rodadas += 1
        linhas()
        acertou = '_' not in letras_acertadas
        enforcou = tentativa == 7

    if acertou:
        imprime_mensagem_ganhador(rodadas, palavra_secreta)
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print('Fim do Jogo')


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
            acertos[index] = letra
    return acertos


def arqexiste(arq):
    try:
        arq = open(arq, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararq(arq):
    try:
        arq = open(arq, 'wt+')
        arq.close()
    except:
        print('Houve um erro ao criar o arquivo')
    else:
        return arq


def gerando_palavra_secreta(arq):
    palavras = []
    with open(arq) as arq:
        for linha in arq:
            palavras.append(linha.strip().upper())
        numero = randrange(0, len(palavras))
    return palavras[numero]


def imprime_mensagem_ganhador(rodadas, palavra_secreta):
    print('Parabens voce ganhou o jogo da forca.')
    print(f'Voce ganhou com {rodadas} rodadas')
    print(f'Palavra chave: {palavra_secreta} ')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print('Voce perdeu, Mais sorte da proxima veiz!')
    print(f'A palavra chave era {palavra_secreta}')
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print('Ate a proxima!')


def desenha_forca(erros):
    print(f'Voce errou!!')
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()
