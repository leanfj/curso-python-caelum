print('**********************')
print('*    Jogo da Forca   *')
print('**********************')

palavra_secreta = 'mandioca'
letras_acertadas = ['_', '_', '_', '_', '_', '_', '_', '_']
enforcou = False
acertou = False

print(letras_acertadas)

while (not enforcou and not acertou):
    chute = input('Qual Letra\n')

    posicao = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            # print('Encontrei a letra {} na posição {}'.format(letra, posicao))
            letras_acertadas[posicao] = letra
        posicao = posicao + 1
    print(letras_acertadas)

print('Fim de Jogo')
