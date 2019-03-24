print('*************************')
print('*  Jogo da Adivinhação  *')
print('*************************')

numero_secreto = 42

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
elif (maior):
    print('Seu chute foi maior')
elif (menor):
    print('Seu chute foi menor')
