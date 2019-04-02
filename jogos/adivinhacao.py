def jogar():
    print('*************************')
    print('*  Jogo da Adivinhação  *')
    print('*************************')

    numero_secreto = 42
    # total_tentativas = 4
    rodada = 1
    total_pontos = 1000

    print('Você tem {}'.format(total_pontos))
    nivel = int(input('Escolha o nivel de dificuldade de 1 a 3\n'))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, total_tentativas))
        chute = int(input('Informe seu chute\n'))
        print('Você digitou: ', chute)

        igual = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        if (igual):
            print('Você acertou e fez {} pontos'.format(total_pontos))
            break
        elif (maior):
            print('Seu chute foi maior e perdeu {} de {}'.format(
                chute, total_pontos))
            total_pontos = abs(total_pontos - chute)
            print('E esta com {}'.format(total_pontos))
        elif (menor):
            print('Seu chute foi menor e perdeu {} de {}'.format(
                chute, total_pontos))
            total_pontos = abs(total_pontos - chute)
            print('E esta com {}'.format(total_pontos))

        rodada = rodada + 1

    print('Fim de Jogo')
