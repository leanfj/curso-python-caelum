def jogar():
    import random
    # Abrindo arquivo no modo leitura
    # arquivo = open('palavras.txt', 'r')
    # Array para receber palavras
    palavras = []
    # Abrindo arquivo e Incluindo cada palavra do arquivo no array
    with open('palavras.txt', 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    # Fechando o uso do arquivo
    # arquivo.close()
    # Gerando numero randomico com range do tamanho do array criado
    numero_randomico = random.randrange(0, len(palavras))

    print('**********************')
    print('*    Jogo da Forca   *')
    print('**********************')

    palavra_secreta = palavras[numero_randomico].upper()
    letras_acertadas = ['_' for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erro = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):
        chute = input('Qual Letra\n')
        chute = chute.strip().upper()
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
