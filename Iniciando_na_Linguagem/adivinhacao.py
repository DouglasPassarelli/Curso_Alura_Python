from random import randint


def jogar():

    cores = ['\033[m', '\033[33m', '\033[31m', '\033[34m', '\033[32m']

    def validacao_nivel(num, msg, cor):
        while True:
            try:
                print(cor[1], end='')
                num = int(input(msg))
                print(cor[0], end='')
            except:
                print(cor[2], end='')
                print('Erro! Apenas numeros são validos, Tente novamente.')
                print(cor[0], end='')
                continue
            else:
                if 0 < num <= 3:
                    return num
                else:
                    print(cor[2], end='')
                    print('Opção Invalida, Voce deve digitar apenas as dificuldades listadas, Tente Novamente.')
                    print(cor[0], end='')
                    continue

    def validacao_chute(num1, msg, cor):
        while True:
            try:
                print(cor[1], end='')
                num1 = int(input(msg))
                print(cor[0], end='')
            except:
                print(cor[2], end='')
                print('Erro! Apenas numeros são validos, Tente novamente.')
                print(cor[0], end='')
                continue
            else:
                if 0 < num1 <= 100:
                    return num1
                else:
                    print(cor[2], end='')
                    print('Opção Invalida,Voce deve digitar um valor de 1 a 100, Tente Novamente.')
                    print(cor[0], end='')
                    continue

    def menu(msg, cor, tam=0):
        tam = len(msg)
        print(cor[3], end='')
        print('*' * tam)
        print(msg)
        print('*' * tam)
        print(cor[0], end='')


    menu('Bem vindo ao jogo de advinhação!', cores)
    pontos = 1000
    total_de_tentativas = n = c = 0
    numero_secreto = randint(1, 100)

    print(cores[1], end='')
    print('Escolha o nivel do Jogo')
    print('(1) Facil   (2) Medio  (3) Dificil')
    print(cores[0], end='')
    nivel = validacao_nivel(n, 'Defina o nivel: ', cores)

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodadas in range(1, total_de_tentativas + 1):
        print(cores[1], end='')
        print(f'Tentativa: {rodadas} de {total_de_tentativas}')
        chute = validacao_chute(c, 'Digite o numero de 1 a 100: ', cores)
        print(cores[1], end='')
        print(f'Voce digitou {chute}')
        print(cores[0], end='')

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(cores[4], end='')
            print('Voce acertou!!')
            print(f'Voce fez um total de {pontos} pontos')
            print(cores[0], end='')
            break
        else:
            pontos_perdidos = abs(chute - numero_secreto)
            pontos -= pontos_perdidos
            if maior:
                print(cores[2], end='')
                print('Voce errou, O chute foi maior que o numero secreto!')
                print(cores[0], end='')
            elif menor:
                print(cores[2], end='')
                print('Voce errou, O chute foi menor que o numero secreto!')
                print(cores[0], end='')

    print(cores[3], end='')
    print(f'O numero secreto é {numero_secreto} e voce fez {pontos} pontos')
    print('Fim do Jogo')
    print(cores[0], end='')


if __name__ == "__main__":
    jogar()
