from random import randint


def jogar():
    def validacao_nivel(num, msg):
        while True:
            try:
                num = int(input(msg))
            except:
                print('Erro! Apenas numeros são validos, Tente novamente.')
                continue
            else:
                if 0 < num <= 3:
                    return num
                else:
                    print('Opção Invalida, Voce deve digitar apenas as dificuldades listadas, Tente Novamente.')
                    continue

    def validacao_chute(num1, msg):
        while True:
            try:
                num1 = int(input(msg))
            except:
                print('Erro! Apenas numeros são validos, Tente novamente.')
                continue
            else:
                if 0 < num1 <= 100:
                    return num1
                else:
                    print('Opção Invalida,Voce deve digitar um valor de 1 a 100, Tente Novamente.')
                    continue

    def menu(msg, tam=0):
        tam = len(msg)
        print('*' * tam)
        print(msg)
        print('*' * tam)

    menu('Bem vindo ao jogo de advinhação!')
    pontos = 1000
    total_de_tentativas = n = c = 0
    numero_secreto = randint(1, 100)

    print('Escolha o nivel do Jogo')
    print('(1) Facil   (2) Medio  (3) Dificil')
    nivel = validacao_nivel(n, 'Defina o nivel: ')

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodadas in range(1, total_de_tentativas + 1):
        print(f'Tentativa: {rodadas} de {total_de_tentativas}')
        chute = validacao_chute(c, 'Digite o numero de 1 a 100: ')
        print(f'Voce digitou {chute}')
        
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

    print(f'O numero secreto é {numero_secreto} e voce fez {pontos} pontos')
    print('Fim do Jogo')


if __name__ == "__main__":
    jogar()
