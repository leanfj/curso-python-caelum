numero = 32
chute = input('Chute um numero\n')
numero_convertido = int(chute)
if numero == numero_convertido:
    print('Você acertou')
else:
    if numero_convertido > numero:
        print('Você errou e seu chute foi maior')
    else:
        print('Você errou e seu chute foi menor')
