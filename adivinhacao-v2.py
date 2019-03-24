numero = 32
chute = input('Chute um numero\n')
numero_convertido = int(chute)

acertou = numero == numero_convertido
maior = numero_convertido > numero
menor = numero_convertido < numero

if acertou:
    print('Você acertou')
elif maior:
    print('Você errou e seu chute foi maior')
elif menor:
    print('Você errou e seu chute foi menor')
