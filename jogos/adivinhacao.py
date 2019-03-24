print('*************************')
print('*  Jogo da Adivinhação  *')
print('*************************')

numero_secreto = 42
total_tentativas = 4
rodada = 1

while (rodada <= total_tentativas):
    print('Tentativa {} de {}'.format(rodada, total_tentativas))
    chute = int(input('Informe seu chute\n'))
    print('Você digitou: ', chute)

    # if (chute == numero_secreto):
    #     print('Você acertou')
    # else:
    #     print('Você Errou')

    # if (chute == numero_secreto):
    #     print('Você Acertou')
    # elif (chute > numero_secreto):
    #     print('Seu chute foi maior')
    # elif (chute < numero_secreto):
    #     print('Seu chute foi menor')
    igual = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if (igual):
        print('Você acertou')
        break
    elif (maior):
        print('Seu chute foi maior')
    elif (menor):
        print('Seu chute foi menor')
    rodada = rodada + 1
    # total_tentativas = total_tentativas - 1
