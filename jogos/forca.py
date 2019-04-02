def jogar():
    print('**********************')
    print('*    Jogo da Forca   *')
    print('**********************')

    palavra_secreta = 'mandioca'
    letras_acertadas = ['_', '_', '_', '_', '_', '_', '_', '_']
    enforcou = False
    acertou = False
    erro = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):
        chute = input('Qual Letra\n')
        if(chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[posicao] = letra
                posicao += 1
        else:
            erro += 1
        enforcou = erro == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)
    if (acertou):
        print('Você ganhou')
    else:
        print('Você perdeu')

    print('Fim de Jogo')
