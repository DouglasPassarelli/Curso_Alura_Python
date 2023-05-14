from random import randint


def jogar():
    def menu(msg, tam=0):
        tam = len(msg)
        print('*' * tam)
        print(msg)
        print('*' * tam)
    menu('Bem vindo ao jogo de advinhação!')
    pontos = 1000
    total_de_tentativas = 0
    numero_secreto = randint(1, 100)

    print('Escolha o nivel do Jogo')
    print('(1) Facil   (2) Medio  (3) Dificil')
    nivel = int(input('Defina o nivel: '))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    for rodadas in range(1, total_de_tentativas + 1):
        print(f'Tentativa: {rodadas} de {total_de_tentativas}')
        chute = int(input('Digite o numero de 1 a 100: '))
        print(f'Voce digitou {chute}')
        if chute < 1 or chute > 100:
            print('Voce deve digitar um valor de 1 a 100!')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print('Voce acertou!!')
            print(f'Voce fez um total de {pontos} pontos')
            break
        else:
            pontos_perdidos = abs(chute - numero_secreto)
            pontos -= pontos_perdidos
            if maior:
                print('Voce errou, O chute foi maior que o numero secreto!')
            elif menor:
                print('Voce errou, O chute foi menor que o numero secreto!')

    print(f'O numero secreto é {numero_secreto} e voce fez {pontos}')
    print('Fim do Jogo')


if __name__ == "__main__":
    jogar()
